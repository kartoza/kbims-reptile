# coding=utf8
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from reptile.models.reptile_collection_record import ReptileCollectionRecord
from reptile.serializers.reptile_collection_serializer import \
    ReptileCollectionSerializer


class ReptileCollectionList(APIView):
    """
    List all reptile collection.
    """

    def get(self, request, *args):
        reptile_collections = ReptileCollectionRecord.objects.filter(
                absent=True)
        serializer = ReptileCollectionSerializer(
                reptile_collections,
                many=True)
        return Response(serializer.data)


class ReptileCollectionDetail(APIView):
    """
    Retrieve a reptile collection instance.
    """

    def get_object(self, pk):
        try:
            return ReptileCollectionRecord.objects.get(pk=pk)
        except ReptileCollectionRecord.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reptile_collection = self.get_object(pk)
        serializer = ReptileCollectionSerializer(reptile_collection)
        return Response(serializer.data)
