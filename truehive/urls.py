from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from user_profile.views import freelancer_page, client_page

urlpatterns = [
    path('profile/', include('user_profile.urls')),
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    # USER PROFILE URLS
    path('profile/freelancer/',
         freelancer_page, name='lancer_account'),
    path('profile/client/', client_page, name='client_account'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
