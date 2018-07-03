# coding=utf-8
"""Reptile collection record model definition.

"""

from bims.models.biological_collection_record import \
    BiologicalCollectionRecord


class ReptileCollectionRecord(BiologicalCollectionRecord):
    """First collection model."""

    # noinspection PyClassicStyleClass
    class Meta:
        """Meta class for project."""
        app_label = 'reptile'
        verbose_name = 'reptile'
        verbose_name_plural = 'reptiles'
