from rest_framework import serializers
from .models import CampaignPost

class CampaignPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignPost
        fields = '__all__'
        lookup_field = 'slug'