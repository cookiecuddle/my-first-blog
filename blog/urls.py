from django.conf.urls import url
from . import views

urlpatterns = [
    (r'^$', views.post_list, name='post_list'),
]
