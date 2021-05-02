from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import AdvertisementPost
from .serializers import AdvertisementPostSerializer

class AdvertisementPostListView(ListAPIView):
    queryset = AdvertisementPost.objects.order_by('-date_created')
    serializer_class = AdvertisementPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class AdvertisementPostDetailView(RetrieveAPIView):
    queryset = AdvertisementPost.objects.order_by('-date_created')
    serializer_class = AdvertisementPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )
