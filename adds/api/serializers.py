from adds.models import Add
from rest_framework import serializers


class AddSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'thumbnail', 'link', 'priority')
        model = Add

