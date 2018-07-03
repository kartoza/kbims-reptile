# coding=utf-8
"""CSV uploader view
"""

import csv
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.gis.geos import Point
from django.views.generic import FormView
from reptile.forms.csv_upload import CsvUploadForm
from bims.models import (
    LocationSite,
    LocationType,
)
from reptile.models.reptile_collection_record import ReptileCollectionRecord


class CsvUploadView(FormView):
    """Csv upload view."""

    form_class = CsvUploadForm
    template_name = 'csv_uploader.html'
    context_data = dict()
    success_url = reverse_lazy('reptile:reptile-csv-upload')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['data'] = self.context_data
        self.context_data = dict()
        return self.render_to_response(context)

    def form_valid(self, form):
        form.save(commit=True)
        reptile_processed = {
            'added': 0,
            'failed': 0
        }

        # Read csv
        csv_file = form.instance.csv_file

        with open(csv_file.path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for record in csv_reader:
                try:
                    location_type, status = LocationType.objects.get_or_create(
                            name='PointObservation',
                            allowed_geometry='POINT'
                    )

                    record_point = Point(
                            float(record['Long']),
                            float(record['Lat']))

                    if 'location_name' in record:
                        location_name = record['location_name']
                    else:
                        location_name = 'No Location Name'

                    location_site, status = LocationSite.objects.get_or_create(
                        location_type=location_type,
                        geometry_point=record_point,
                        name=location_name,
                    )

                    # Get existed taxon
                    collections = ReptileCollectionRecord.objects.filter(
                            original_species_name=record['Taxon']
                    )

                    taxon_gbif = None
                    if collections:
                        taxon_gbif = collections[0].taxon_gbif_id

                    collection, collection_status = ReptileCollectionRecord.\
                        objects.get_or_create(
                            site=location_site,
                            original_species_name=record['Taxon'],
                            present=True,
                            collection_date=datetime.strptime(
                                    record['date'], '%d %b %Y'),
                            collector=record['Observer'],
                            notes=record['notes'],
                            taxon_gbif_id=taxon_gbif,
                        )
                    if collection_status:
                        reptile_processed['added'] += 1
                except (ValueError, KeyError):
                    reptile_processed['failed'] += 1

        self.context_data['uploaded'] = 'Reptile added ' + \
                                        str(reptile_processed['added'])
        return super(CsvUploadView, self).form_valid(form)
