from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^programinfo$', views.info),
    url(r'^process$', views.process)
]