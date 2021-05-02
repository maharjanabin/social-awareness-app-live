from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from campaign.models import CampaignPost
from campaign.serializers import CampaignPostSerializer

class CampaignPostListView(ListAPIView):
    queryset = CampaignPost.objects.order_by('-date_created')
    serializer_class = CampaignPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class CampaignPostDetailView(RetrieveAPIView):
    queryset = CampaignPost.objects.order_by('-date_created')
    serializer_class = CampaignPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class CampaignPostFeaturedView(ListAPIView):
    queryset = CampaignPost.objects.all().filter(featured=True)
    serializer_class = CampaignPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class CampaignPostCategoryView(APIView):
    serializer_class = CampaignPostSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = CampaignPost.objects.order_by('-date_created').filter(category__iexact=category)

        serializer = CampaignPostSerializer(queryset, many=True)

        return Response(serializer.data)

class CampaignPostCreateView(CreateAPIView):
    queryset = CampaignPost.objects.all()
    serializer_class = CampaignPostSerializer
    permission_classes = (permissions.AllowAny, )