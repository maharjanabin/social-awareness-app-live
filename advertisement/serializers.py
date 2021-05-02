from rest_framework import serializers
from .models import AdvertisementPost

class AdvertisementPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementPost
        fields = '__all__'
        lookup_field = 'slug'