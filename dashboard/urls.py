from django.urls import path, include
from .views import index, projects_view, notifications_view, account_edit_view, notification_refs, project_detail, project_edit, project_delete, projects_create_view, project_bids, project_assignment
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'

urlpatterns = [
    path('', index),
    path('account/edit/', account_edit_view),
    path('notifications/', notifications_view),
    path('notifications/read/<int:notification_id>/', notification_refs),
    path('projects/', projects_view),
    path('projects/new/', projects_create_view),
    path('projects/<int:project_id>/', project_detail),
    path('projects/<int:project_id>/edit/', project_edit),
    path('projects/<int:project_id>/delete/', project_delete),
    path('projects/<int:project_id>/bids/', project_bids),
    path('projects/<int:project_id>/assign/<int:user_id>/', project_assignment),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
