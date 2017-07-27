from django.conf.urls import url
from . import views

urlpatterns = [
    (r'^$', viewsviews.post_list, name='post_list'),
]
