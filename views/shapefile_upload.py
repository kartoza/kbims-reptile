from bims.views.shapefile_upload import \
    ShapefileUploadView, process_shapefiles
from reptile.models.reptile_collection_record import ReptileCollectionRecord


class ShapefileUploadView(ShapefileUploadView):
    template_name = 'reptile_shapefile_uploader.html'


def reptile_process_shapefiles(request):
    additional_fields = {
        'present': 'bool',
        'absent': 'bool',
    }
    return process_shapefiles(
            request=request,
            collection=ReptileCollectionRecord,
            additional_fields=additional_fields)
