from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.template.defaulttags import csrf_token
from .models import Place, People

# @login_required(login_url='credentials/login')
def demo(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    places = Place.objects.all()
    peoples = People.objects.all()
    return render(request, 'index.html', {'places': places, 'peoples': peoples})

# def add(request):
#     num1 = int(request.GET['num1'])
#     num2 = int(request.GET['num2'])
#     added = num1 + num2
#     subtracted = num1 - num2
#     multiplied = num1 * num2
#     divided = 'inf' if num2 == 0 else num1/num2
#     return render(request, 'add.html', {'num1': num1, 'num2': num2, 'add': added, 'sub': subtracted, 'mul': multiplied, 'div': divided})

# def contact(request):
#     return render(request, 'contact.html')