from django.urls import path
from .views import AdvertisementPostListView, AdvertisementPostDetailView

urlpatterns = [
    path('', AdvertisementPostListView.as_view()),
    path('<slug>', AdvertisementPostDetailView.as_view()),
]