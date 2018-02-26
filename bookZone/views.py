from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Book,Author,Category,rateBook

from bookZone.forms import SignUpForm


def welcome(request):
    return render(request,'bookZone/welcome.html')

def index(request):
    if request.user.is_authenticated:
        return render(request,'bookZone/index.html', {'name':'name'})
    else:
        return redirect('welcome')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'bookZone/index.html', {'form': form})
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})

def category(request,**kwargs):
    if len(kwargs) == 0:
        category = Category.objects.all()
        one = "many";
        for cat in category:
            cat.pic = cat.cat_pic.url.replace("bookZone/","/",1)
            category.fav = category.Users.filter(pk=request.user.id)
        return render(request, 'bookZone/category.html',{'categories': category,'one':one})

    else:
        category = Author.objects.filter(id=kwargs['id'])
        one = "one"
        for cat in category:
            cat.pic = category.cat_pic.url.replace("bookZone/","/",1)
            cat.fav = category.Users.filter(pk=request.user.id)
        return render(request, 'bookZone/category.html',{'categories': category,'one':one})


    return render(request, 'bookZone/category.html',{'categories': category})

def book(request,category_id):
    book = Book.objects.filter(categories=category_id)
    return render(request, 'bookZone/book.html',{'books': book})


def author(request,**kwargs):
    if len(kwargs) == 0:
        authors = Author.objects.all()
        one = "many";
        for author in authors:
            author.pic = author.author_pic.url.replace("bookZone/","/",1)
        return render(request, 'bookZone/authors.html',{'authors': authors,'one':one})
    else:
        authors = Author.objects.filter(id=kwargs['id'])
        one = "one"
        for author in authors:
            author.pic = author.author_pic.url.replace("bookZone/","/",1)
            author.isFollowed = author.users.filter(pk=request.user.id)
        return render(request, 'bookZone/authors.html',{'authors': authors,'one':one})

def follow(request,**kwargs):
    author = Author.objects.get(pk=kwargs['author_id'])
    if kwargs['follow'] == "follow":
        author.users.add(request.user.id)
    elif kwargs['follow'] == "unfollow":
        author.users.remove(request.user)
    return redirect('/bookZone/authors/'+str(kwargs['author_id']),{'authors': author})


def fav(request,**kwargs):
    category = Category.objects.get(pk=kwargs['category_id'])
    if kwargs['fav'] == "fav":
        Category.users.add(request.user.id)
    elif kwargs['fav'] == "nofav":
        Category.users.remove(request.user)
    return redirect('/bookZone/category/'+str(kwargs['category_id']),{'category': category})
