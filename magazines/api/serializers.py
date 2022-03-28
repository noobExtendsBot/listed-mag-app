from rest_framework import serializers
from magazines.models import MagazinePost


class MagazineSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = MagazinePost