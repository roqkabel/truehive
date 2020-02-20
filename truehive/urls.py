from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from user_profile.views import freelancer_page, client_page
from dashboard.views import index
from django.views.static import serve

urlpatterns = [
    path('profile/', include('user_profile.urls')),
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    # USER PROFILE URLS
    path('profile/freelancer/',
         freelancer_page, name='lancer_account'),
    path('profile/client/', client_page, name='client_account'),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
                'document_root': settings.MEDIA_ROOT,
                }),
    ]
