# coding=utf-8
"""Tests for models."""
from django.test import TestCase
from reptile.tests.model_factories import (
    ReptileCollectionRecordF,
)


class TestReptileCollectionRecordCRUD(TestCase):
    """
    Tests reptile collection record.
    """
    def setUp(self):
        """
        Sets up before each test
        """
        pass

    def test_ReptileCollectionRecord_create(self):
        """
        Tests reptile collection record creation
        """

        model = ReptileCollectionRecordF.create()

        # check if pk exists
        self.assertTrue(model.pk is not None)

        # check if site exists
        self.assertTrue(model.site is not None)

        # check if original species name exists
        self.assertTrue(model.original_species_name is not None)

    def test_ReptileCollectionRecord_read(self):
        """
        Tests reptile collection record model read
        """
        model = ReptileCollectionRecordF.create(
            habitat=u'freshwater',
            original_species_name=u'custom original_species_name',
            present=False,
        )

        self.assertTrue(model.habitat == 'freshwater')
        self.assertTrue(
                model.original_species_name == 'custom original_species_name')

    def test_ReptileCollectionRecord_update(self):
        """
        Tests reptile collection record model update
        """
        model = ReptileCollectionRecordF.create()
        new_data = {
            'habitat': u'freshwater',
            'original_species_name': u'custom original_species_name update',
            'present': False,
        }
        model.__dict__.update(new_data)

        # check if updated
        for key, val in new_data.items():
            self.assertEqual(model.__dict__.get(key), val)

    def test_ReptileCollectionRecord_delete(self):
        """
        Tests reptile collection record model delete
        """
        model = ReptileCollectionRecordF.create()
        model.delete()

        # check if deleted
        self.assertTrue(model.pk is None)
