from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^register/$', views.register_book, name='register_book'),
    url(r'^issue/(?P<pk>\d+)/$', views.issue_book, name='issue_book'),
    url(r'^return/$', views.return_book, name='return_book'),
    url(r'^index/search/$', views.search_book, name='search'),
    url(r'^index/$', views.index, name='index'),
    url(r'^issued-list/$', views.issued_books, name='issued_books'),
    #url(r'^import-csv/$', views.import_csv, name='import-csv'),
    url(r'^$', views.user_login, name='login'),

   
]