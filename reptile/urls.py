# coding=utf-8

from django.conf.urls import url
from reptile.api_views.reptile_collection_record import (
    ReptileCollectionList,
    ReptileCollectionDetail,
)
from django.contrib.auth.decorators import login_required
from reptile.views.csv_upload import CsvUploadView


api_urls = [
    url(r'^api/reptile-collections/$', ReptileCollectionList.as_view()),
    url(r'^api/reptile-collections/(?P<pk>[0-9]+)/$',
        ReptileCollectionDetail.as_view()),
    url(r'^reptile/upload/$',
        login_required(CsvUploadView.as_view()),
        name='reptile-csv-upload'),
]

urlpatterns = [
# Add custom URL paths here 

] + api_urls
