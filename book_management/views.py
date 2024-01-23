from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from book_management.models import *
from book_management.forms import *
from book_management.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

def home(request):
    return render(request, 'home.html')

def book_list(request):
    blist = BookEntity.objects.all()
    return render(request, 'book_list.html', context={'blist':blist})

def author_list(request):
    alist = AuthorEntity.objects.all()
    return render(request, 'author_list.html', context={'alist':alist})

def add_book_list(request):
    bform = BookEntityForm()
    if request.method == "POST":
        bform1 = BookEntityForm(request.POST)
        if bform1.is_valid():
            bform1.save()
            blist = BookEntity.objects.all()
        return render(request, 'book_list.html', context={'blist':blist})
    return render(request, 'add_book_list.html', context={'bform':bform})

def add_author_list(request):
    aform = AuthorEntityForm()
    if request.method == "POST":
        aform1 = AuthorEntityForm(request.POST)
        if aform1.is_valid():
            aform1.save()
            alist = AuthorEntity.objects.all()
        return render(request, 'author_list.html', context={'alist':alist})
    return render(request, 'add_author_list.html', context={'aform':aform})

def edit_author_list(request, id):
    a = AuthorEntity.objects.get(id = id)
    return render(request, 'edit_author_list.html', context={'a': a})

def edit_book_list(request, id):
    b = BookEntity.objects.get(id = id)
    alist = AuthorEntity.objects.all()
    return render(request, 'edit_book_list.html', context={'b': b, 'alist':alist})

def update_author_list(request, id):
    a = AuthorEntity.objects.get(id = id)
    form1 = AuthorEntityForm(request.POST, instance=a)
    if form1.is_valid():
        form1.save()
        alist = AuthorEntity.objects.all()
        return render(request, 'author_list.html', context={'alist':alist})
    else:
        return HttpResponse("<h1>not valid</h1>")
    
def update_book_list(request, id):
    b = BookEntity.objects.get(id = id)
    bform1 = BookEntityForm(request.POST, instance=b)
    if bform1.is_valid():
        bform1.save()
        blist = BookEntity.objects.all()
        return render(request, 'book_list.html', context={'blist':blist})
    else:
        return HttpResponse("<h1>not valid</h1>")

def delete_author_list(request, id):
    AuthorEntity.objects.filter(id=id).delete()
    alist = AuthorEntity.objects.all()
    return render(request, 'author_list.html', context={'alist':alist})

def delete_book_list(request, id):
    BookEntity.objects.filter(id= id).delete()
    blist = BookEntity.objects.all()
    return render(request, 'book_list.html', context={'blist':blist})

@csrf_exempt
def author_ser(request):
    data = AuthorEntity.objects.all()
    if request.method == 'GET':
        a = AuthorEntitySerializer(data, many=True)
        return JsonResponse(a.data, safe=False)
    elif request.method == 'POST':
        input_data = JSONParser().parse(request)
        s = AuthorEntitySerializer(data=input_data)
        if s.is_valid():
            s.save()
        return JsonResponse(s.data)
    
@csrf_exempt
def book_ser(request):
    data = BookEntity.objects.all()
    if request.method == 'GET':
        a = BookEntitySerializer(data, many=True)
        return JsonResponse(a.data, safe=False)
    elif request.method == 'POST':
        input_data = JSONParser().parse(request)
        s = BookEntitySerializer(data=input_data)
        if s.is_valid():
            s.save()
        return JsonResponse(s.data)
    
@csrf_exempt
def SingleAuthor(request, id):
    data = AuthorEntity.objects.get(id=id)
    if request.method == "GET":
        a = AuthorEntitySerializer(data)
        return JsonResponse(a.data)
    elif request.method == "PUT":
        input_data = JSONParser().parse(request)
        s = AuthorEntitySerializer(data, data=input_data)
        if s.is_valid():
            s.save()
        return JsonResponse(s.data)
    elif request.method == "DELETE":
        data.delete()
        return HttpResponse("DELETED")
    
@csrf_exempt
def SingleBook(request, id):
    data = BookEntity.objects.get(id=id)
    if request.method == "GET":
        a = BookEntitySerializer(data)
        return JsonResponse(a.data)
    elif request.method == "PUT":
        input_data = JSONParser().parse(request)
        s = BookEntitySerializer(data, data=input_data)
        if s.is_valid():
            s.save()
        return JsonResponse(s.data)
    elif request.method == "DELETE":
        data.delete()
        return HttpResponse("DELETED")
    

