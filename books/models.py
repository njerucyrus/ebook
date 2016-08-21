from django.db import models


class BookCategory(models.Model):
    category = models.CharField(max_length=50)
    category_slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.category


class Book(models.Model):
    book_no = models.CharField(max_length=20, db_index=True, unique=True)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    available = models.BooleanField(default=True)
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.book_no)


class BooksIssued(models.Model):
    book = models.OneToOneField(Book, verbose_name="Book No")
    phone_no = models.CharField(max_length=13)
    reg_no = models.CharField(max_length=20)
    date_issued = models.DateTimeField(auto_now_add=True)
    # Will change latter after implementation
    return_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Books Issued'

    def __str__(self):
        return str(self.book)


# stores the number of times a book has been issued out.
class BookCount(models.Model):
    book_no = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.book_no)




