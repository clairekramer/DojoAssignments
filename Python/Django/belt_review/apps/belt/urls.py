from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^users/(?P<id>/d+)$', views.user, name='user'),
    url(r'^logout$', views.logout, name='logout'),
]
