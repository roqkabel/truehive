from django.conf.urls.static import static
from django.urls import path, include
from .views import index

app_name = 'user_profile'

urlpatterns = [
    path('', index),
    # path('how-it-works/', how_it_works, name="how_it_works"),
]
