from django.contrib import admin
from books.models import Book, BooksIssued, BookCount, BookCategory


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'category_slug']
    prepopulated_fields = {'category_slug': ('category',)}

    class Meta:
        model = BookCategory
admin.site.register(BookCategory, BookCategoryAdmin)



class BookAdmin(admin.ModelAdmin):
    list_display = ['book_no', 'title', 'category', 'author', 'publisher', 'available']

    class Meta:
        model = Book
admin.site.register(Book, BookAdmin)


class BooksIssuedAdmin(admin.ModelAdmin):
    list_display = ['book', 'phone_no', 'reg_no', 'date_issued', 'return_date']

    class Meta:
        model = BooksIssued
admin.site.register(BooksIssued, BooksIssuedAdmin)


class BookCountAdmin(admin.ModelAdmin):
    list_display = ['book_no', 'count']

    class Meta:
        model = BookCount
admin.site.register(BookCount, BookCountAdmin)

#
# class BookAdminImporter(forms.ModelForm):
# 	class Meta:
# 		model = Book
# 		fields = ('book_no', 'title', 'category', 'author', 'publisher',)
#
# class BooksCsvAdmin(ImportCSVModelAdmin):
# 	importer_class = BookAdminImporter
# admin.site.register(Book, BooksCsvAdmin)


