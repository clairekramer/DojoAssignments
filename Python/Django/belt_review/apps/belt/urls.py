from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^books$', views.books, name='books'),
    url(r'^books/add$', views.add_book, name='add_book'),
    url(r'^books/create$', views.create, name='new_book'),
    url(r'^books/(?P<id>/d+)$', views.book_page, name='one_book'),
    url(r'^users/(?P<id>/d+)$', views.user, name='user')
]
