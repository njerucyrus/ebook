from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^books/$', views.BookList.as_view()),
    url(r'^books/(?P<pk>[0-9|a-zA-Z]+)$', views.BookDetail.as_view()),
    url(r'^issued/$', views.BooksIssuedList.as_view()),
    url(r'^issued/(?P<pk>[0-9]+)$', views.BooksIssuedDetail.as_view()),
    url(r'^count/$', views.BookCountList.as_view()),
    url(r'^count/(?P<pk>[0-9]+)$', views.BookCountDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)