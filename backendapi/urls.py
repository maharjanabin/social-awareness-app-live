from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin', admin.site.urls),
    path('campaign/', include('campaign.urls')),
    path('advertisement/', include('advertisement.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('user_profile.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
]
