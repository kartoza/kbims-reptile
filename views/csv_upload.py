# coding=utf-8
"""CSV uploader view
"""

from django.urls import reverse_lazy
from bims.views.csv_upload import CsvUploadView as BaseCsvUploadView
from reptile.models.reptile_collection_record import ReptileCollectionRecord


class CsvUploadView(BaseCsvUploadView):
    """Csv upload view."""

    collection_record = ReptileCollectionRecord
    template_name = 'reptile_csv_uploader.html'
    success_url = reverse_lazy('reptile:reptile-csv-upload')
    additional_fields = {
        'present': 'bool',
        'absent': 'bool',
    }
