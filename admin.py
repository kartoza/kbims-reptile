# coding=utf-8

from django.contrib import admin
from reptile.models import (
    ReptileCollectionRecord,
    CSVDocument,
)


class ReptileCollectionAdmin(admin.ModelAdmin):
    list_display = (
        'original_species_name',
        'category',
        'collection_date',
        'owner',
    )


admin.site.register(ReptileCollectionRecord, ReptileCollectionAdmin)
admin.site.register(CSVDocument)
