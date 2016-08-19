from django import forms
from books.models import Book, BooksIssued


class RegisterBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_no', 'title', 'category', 'author', 'publisher')


class IssueBookForm(forms.ModelForm):
    # book_no = forms.CharField(max_length=20)
    # phone_number = forms.CharField(max_length=13)
    # reg_no = forms.CharField(max_length=20)
    class Meta:
        model = BooksIssued
        fields = ('book_no', 'phone_number', 'reg_no')


class ReturnBookForm(forms.Form):
    book_no = forms.CharField(max_length=20)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# import many books into the database from a csv file
# class ImportBooksForm(forms.ModelForm):
#     file_to_import = forms.FileField()
#
#     class Meta:
#         model = Book
#         fields = ('file_to_import', )
#
#     def save(self, commit=False, *args, **kwagrs):
#         form = ImportBooksForm()
#         file_csv = request.FILES('file_to_import')
#         data_file = open(file_csv, 'rb')
#         records = csv.reader(data_file)
#         for line in records:
#             self.book_no = line[1]
#             self.title = line[2]
#             self.category = line[3]
#             self.author = line[4]
#             self.publisher = line[5]
#             form.save()
#         data_file.close()




