from rest_framework import serializers
from reptile.models import ReptileCollectionRecord


class ReptileCollectionSerializer(serializers.ModelSerializer):
    """
    Serializer for reptile collection model.
    """
    owner = serializers.SerializerMethodField()

    def get_owner(self, obj):
        if obj.owner:
            return '%s,%s' % (obj.owner.pk, obj.owner.username)

    class Meta:
        model = ReptileCollectionRecord
        fields = '__all__'
