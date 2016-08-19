from django.shortcuts import render, HttpResponse
from books.forms import *
from django.db.models import Q
from books.models import *
from django.contrib.auth import *


def register_book(request):
    if request.method == 'POST':
        form = RegisterBookForm(request.POST)
        if form.is_valid():
            bk_count = BookCount()
            bk_count.book_no = request.POST.get('book_no', '')
            form.save()
            bk_count.save()
            return HttpResponse("Book Saved Successfully!")
    else:
        form = RegisterBookForm()
    return render(request, 'register_book.html', {'form': form})


def issue_book(request):
    return

def return_book(request):
    if request.method == 'POST':
        form = ReturnBookForm(request.POST)
        if form.is_valid():
            book_no = request.POST.get('book_no', '')
            try:
                book_issued = BooksIssued.objects.get(book_no=book_no)
                book_count = BookCount.objects.get(book_no=book_no)
                book = Book.objects.get(book_no=book_no)
                book.available = True
                book_count.count += 1
                book_count.save()
                book.save()
                book_issued.delete()
                return HttpResponse(
                    'book was book no {} was Successfully Returned.'.format(request.POST.get('book_no', '')))
            except BooksIssued.DoesNotExist as e:
                return HttpResponse("No such book was issued {0}:-)".format(str(e)))
    else:
        form = ReturnBookForm()
    return render(request, 'return_book.html', {'form': form, })


def search_book(request):
    query = request.GET.get('q', '')
    if query:
        query_set = (
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(publisher__icontains=query) |
            Q(category__icontains=query)
        )
        results = Book.objects.filter(query_set).distinct()
    else:
        results = []
    return render_to_response('search.html', {'results': results, 'query': query, })


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


def issued_books(request):
    bks = BooksIssued.objects.all()
    return render(request, 'books_issued.html', {'books': bks, })
