from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from books.forms import NewBookForm, SearchForm, AddBookForm
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count

def userLogin(request):
    data = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("User Name:", username,"\nPassword:", password)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('http://localhost:8000/books/home/')
        else:
            data['error']='User name or password is incorrect'
            return render(request, 'books/login_book.html')
    else:
        return render(request, 'books/login_book.html', data)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/books/userlogin/')

@login_required(login_url='http://localhost:8000/books/userlogin/')
def viewHome(request):
    books = Book.objects.values('title').distinct().order_by('title')
    query_set = Book.objects.all().values('title').annotate(total=Count('title')).order_by('title')
    print("QuerySet:::::", query_set)
    dict = {'books':books, 'count':query_set}
    res = render(request, 'books/index.html', dict)
    return res

    #variable = Book.objects.all()
    #count_specific1 = Book.objects.filter(title='C').count()
    #count_specific2 = Book.objects.filter(title='C++').count()
    #count_specific3 = Book.objects.filter(title='Java').count()
    #count_specific4 = Book.objects.filter(title='DBMS').count()
    #count_specific5 = Book.objects.filter(title='Operating system').count()
    #count_specific6 = Book.objects.filter(title='Math').count()
    #dict = {'bookdata':variable, 'count_specific1':count_specific1, 'count_specific2':count_specific2,'count_specific3':count_specific3,'count_specific4':count_specific4,'count_specific5':count_specific5,'count_specific6':count_specific6}
    #res = render(request, 'books/index.html', dict)
    #return HttpResponse(res)

@login_required(login_url='http://localhost:8000/books/userlogin/')
def viewBook(request):
    book_data = Book.objects.all()
    count_book = Book.objects.all().count()
    #print("\n\nReturn:=", book_data.query)
    #print("\n\nSQL Query:=", book_data.query)
    dict = {'book_data':book_data, 'count_book':count_book}
    res1 = render(request, 'books/view_book.html', dict)
    return res1

@login_required(login_url='http://localhost:8000/books/userlogin/')
def editBook(request):
    book = Book.objects.get(id=request.GET['bookid'])
    fields = {'title':book.title, 'price':book.price, 'author':book.author, 'publisher':book.publisher}
    form = NewBookForm(initial=fields)
    res = render(request, 'books/edit_book.html', {'form':form, 'book':book})
    return res

@login_required(login_url='http://localhost:8000/books/userlogin/')
def update(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST)
        book = Book()
        book.id = request.POST['book_id']
        book.title = form.data['title']
        book.price = form.data['price']
        book.author = form.data['author']
        book.publisher = form.data['publisher']
        book.save()
        return HttpResponseRedirect('http://localhost:8000/books/view/')

@login_required(login_url='http://localhost:8000/books/userlogin/')
def deleteBook(request):
    bookid = request.GET['bookid']
    book = Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('http://localhost:8000/books/view/')

@login_required(login_url='http://localhost:8000/books/userlogin/')
def searchForm(request):
    take_form = SearchForm()
    dict = {'form':take_form}
    res = render(request, 'books/search_book.html', dict)
    return res

@login_required(login_url='http://localhost:8000/books/userlogin/')
def search(request):
    take_form_value = SearchForm(request.POST)
    books = Book.objects.filter(title=take_form_value.data['title'])
    dict = {'form':take_form_value, 'books':books}
    res = render(request, 'books/search_book.html', dict)
    return res

@login_required(login_url='http://localhost:8000/books/userlogin/')
def insertBook(request):
    # Take form from NewBookForm class
    form_var = NewBookForm()
    dict = {'form_var':form_var}
    # here python form give to html file
    res = render(request,'books/insert_book.html', dict)
    return res

@login_required(login_url='http://localhost:8000/books/userlogin/')
def insert(request):
    if request.method =='POST':
        form = NewBookForm(request.POST)
        book = Book()
        book.title = form.data['title'].title()
        book.price = form.data['price']
        book.author = form.data['author'].title()
        book.publisher = form.data['publisher']
        book.datetime = form.data['datetime']
        book.save()
    res = render(request, 'books/insert_book.html')
    return res
