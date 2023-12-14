from .models import *
from rest_framework import serializers


class KvartiriListSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField()


    class Meta:
        model = Kvartiri
        fields = (
            'title',
            'district',
            'address',
            'city',
            'phone',
            'rooms',
            'price',
            'main_image',
            'id',

            'kond',
            'tehnika',
            'posuda',
            'stiralka',
            'wifi',
            'tv',
            'holodilnik',
            'micro',
            'tea',
            'utug'
        )