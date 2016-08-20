from django.shortcuts import *
from books.forms import *
from django.db.models import Q
from books.models import *
from django.contrib.auth import *


def register_book(request):
    if request.method == 'POST':
        form = RegisterBookForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            book_no = cd['book_no']

            form.save()
            book = Book.objects.get(book_no=book_no)

            bcount = BookCount.objects.create(
                book_no=book,
                count=0
            )
            bcount.save()

            return HttpResponse("Book Saved Successfully!")
    else:
        form = RegisterBookForm()
    return render(request, 'register_book.html', {'form': form})


def issue_book(request, pk):
    book = Book.objects.get(pk=pk)
    book_no = book.book_no
    form_args = {'book_no': book_no, }
    if request.method == 'POST':
        form = IssueBookForm(request.POST, initial=form_args)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                issued_bk = BooksIssued.objects.create(
                    book=book,
                    phone_no=cd['phone_no'],
                    reg_no=cd['reg_no']
                )
                book.available = False
                issued_bk.save()
                book.save()
                return HttpResponse("book issued Successfully")

            except:

                return HttpResponse("Error! book already issued out.")
    else:
        form = IssueBookForm(initial=form_args)
    return render(request, 'issue_book.html', {'form': form, })


def books_issued_list(request):
    bks = BooksIssued.objects.all()
    return render(request, 'books_issued.html', {'bks': bks, })


def return_book(request, pk):
    # get issued book
    try:
        book = Book.objects.get(pk=pk)
        book_issued = BooksIssued.objects.get(book=book)
        book_count = BookCount.objects.get(book_no=book)

        if book_count is not None:
            book_count.count += 1
            book_count.save()
            book_issued.delete()
            book.available = True
            book.save()
            return HttpResponse("Book returned successfully.")

        else:
            book_count = BookCount.objects.create(
                book_no=book,
                count=1
            )
            book_count.save()
            book_issued.delete()
            return HttpResponse("Book returned successfully.")
    except Exception as e:

        return HttpResponse("Error occurred book not returned")


def search_book(request):
    query = request.GET.get('q', '')
    if query:
        query_set = (
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(publisher__icontains=query) |
            Q(category__icontains=query)
            # Q(available=True)
        )
        results = Book.objects.filter(query_set).distinct()
    else:
        results = []
    return render_to_response('index.html', {'results': results, 'query': query, })


def index(request):
    available_books = Book.objects.filter(available=True)
    return render(request, 'index.html', {'books': available_books, })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # get the cleaned data
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                # check if the user is active
                if user.is_active:
                    login(request, user)
                    # provide the login url for redirect
                    return HttpResponseRedirect('/index/')
                else:
                    return HttpResponse('Account is dissabled Contact Admin')
            else:
                return HttpResponse('Login Successful!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, })


