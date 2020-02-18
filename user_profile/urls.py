from django.urls import path, include
from .views import index, freelancer_page, client_page

app_name = 'user_profile'

urlpatterns = [
    path('', index, name='user_index'),

]
