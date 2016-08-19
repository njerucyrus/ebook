from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from books.api.serializers import *
from books.models import *


# views for api
class BookList(generics.ListCreateAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BooksIssuedList(generics.ListCreateAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = BooksIssued.objects.all()
    serializer_class = BooksIssuedSerializer


class BooksIssuedDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = BooksIssued.objects.all()
    serializer_class = BooksIssuedSerializer


class BookCountList(generics.ListCreateAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = BookCount.objects.all()
    serializer_class = BookCountSerializer


class BookCountDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = BookCount.objects.all()
    serializer_class = BookCountSerializer
