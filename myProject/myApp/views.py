from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def detail(request):
    book_list = Book.object.order_by('-pub_date')[:5]
    context = {'book_list': book_list}
    return render(request, 'myApp/detail.html', context)