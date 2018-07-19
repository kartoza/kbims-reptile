# coding=utf-8

from django.conf.urls import url
from reptile.api_views.reptile_collection_record import (
    ReptileCollectionList,
    ReptileCollectionDetail,
)
from django.contrib.auth.decorators import login_required
from reptile.views.csv_upload import CsvUploadView
from reptile.views.shapefile_upload import (
    ShapefileUploadView,
    reptile_process_shapefiles
)


api_urls = [
    url(r'^api/reptile-collections/$', ReptileCollectionList.as_view()),
    url(r'^api/reptile-collections/(?P<pk>[0-9]+)/$',
        ReptileCollectionDetail.as_view()),
    url(r'^reptile/upload/$',
        login_required(CsvUploadView.as_view()),
        name='reptile-csv-upload'),
    url(r'^reptile/upload_shp/$',
        login_required(ShapefileUploadView.as_view()),
        name='reptile-shapefile-upload'),
    url(r'^reptile/process_shapefiles/$', reptile_process_shapefiles,
        name='reptile-process_shapefiles'),
]

urlpatterns = api_urls
