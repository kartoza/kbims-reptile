from django.test import TestCase
from rest_framework.test import APIRequestFactory
from reptile.tests.model_factories import (
    ReptileCollectionRecordF,
)
from reptile.api_views.reptile_collection_record import (
    ReptileCollectionList,
    ReptileCollectionDetail
)


class TestApiView(TestCase):
    """Test Reptile API """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.reptile_collection_1 = ReptileCollectionRecordF.create(
            pk=1,
            original_species_name=u'Test reptile species name 1',
        )
        self.reptile_collection_2 = ReptileCollectionRecordF.create(
            pk=2,
            original_species_name=u'Test reptile species name 2',
        )

    def test_get_all_reptile(self):
        view = ReptileCollectionList.as_view()
        request = self.factory.get('/api/reptile-collections/')
        response = view(request)
        self.assertTrue(len(response.data) > 1)

    def test_get_reptile_by_id(self):
        view = ReptileCollectionDetail.as_view()
        pk = 1
        request = self.factory.get('/api/reptile-collections/' + str(pk))
        response = view(request, str(pk))
        self.assertEqual(
            self.reptile_collection_1.original_species_name,
            response.data['original_species_name']
        )
