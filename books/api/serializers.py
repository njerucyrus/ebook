from rest_framework import serializers
from books.models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_no', 'title', 'category', 'author', 'publisher', 'date_recorded')


class BooksIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model = BooksIssued


