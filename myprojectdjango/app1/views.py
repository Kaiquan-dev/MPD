from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from app1.models import User
from app1.models import Book
from datetime import date

 
def forma(request):
    return render(request, "forma.html")
 
def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")


def index_data(request):
    x = {"kochis": "gay", "id": 1}

    return JsonResponse(x)

def my_index(request):
    return render(request, 'index.html')


def index_users(request):
    all_users = User.objects.all()
    return render(request, 'users.html', locals())


def index_books(request):
    all_books = Book.objects.all()
    return render(request, 'books.html', locals())


def current_user(request, id):
    current_user = User.objects.get(id=id)
    

    age = (date.today() - current_user.birthdate).days // 365
    return render(request, 'current_user.html', locals())
