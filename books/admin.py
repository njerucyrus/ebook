from django.contrib import admin
from books.models import Book, BooksIssued, BookCategory


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'category_slug']
    prepopulated_fields = {'category_slug': ('category',)}

    class Meta:
        model = BookCategory
admin.site.register(BookCategory, BookCategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['book_no', 'title', 'category', 'author', 'publisher', 'available', 'count']

    class Meta:
        model = Book
admin.site.register(Book, BookAdmin)


class BooksIssuedAdmin(admin.ModelAdmin):
    list_display = ['book', 'phone_no', 'reg_no', 'date_issued', 'return_date']

    class Meta:
        model = BooksIssued
admin.site.register(BooksIssued, BooksIssuedAdmin)





