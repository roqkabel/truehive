from django.urls import path, include
from .views import index, projects_view, project_detail, project_edit, project_delete, projects_create_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'

urlpatterns = [
    path('', index),
    path('projects/', projects_view),
    path('projects/new/', projects_create_view),
    path('projects/<int:project_id>', project_detail),
    path('projects/<int:project_id>/edit', project_edit),
    path('projects/<int:project_id>/delete', project_delete)
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
