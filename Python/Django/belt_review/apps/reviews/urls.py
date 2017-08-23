from django.conf.urls import url
from . import views

urlpatterns = [
        #URLS for Books and Reviews
        url(r'^$', views.books, name='books'),
        url(r'^add$', views.add_book, name='add_book'),
        url(r'^create$', views.create, name='new_book'),
        url(r'^(?P<book_id>\d+)$', views.book_page, name='one_book'),
        url(r'^(?P<book_id>\d+)/create$', views.create_additional)
]
