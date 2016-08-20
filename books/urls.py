from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.register_book, name='register_book'),
    url(r'^issue-book/(?P<pk>\d+)/$', views.issue_book, name='issue_book'),
    url(r'^return-book/(?P<pk>\d+)/$', views.return_book, name='return_book'),
    url(r'^books-issued/$', views.books_issued_list, name='books_issued_list'),
    url(r'^index/search/$', views.search_book, name='search'),
    url(r'^$', views.user_login, name='login'),

   
]