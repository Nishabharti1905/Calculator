from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def addfun(request):
    n1 = 10
    n2 = 20
    n3 = n1+n2
    return HttpResponse(f"add page <br/>  n1={n1},n2={n2} and sum={n3}")


def subfun(request):
    n1 = 10
    n2 = 20
    n3 = n1 - n2
    return HttpResponse(f"<h1>sub page</h1> <br/>  n1={n1},n2={n2} and sum={n3}")


def mulfun(request):
    n1 = 10
    n2 = 20
    n3 = n1 * n2
    return HttpResponse(f"Multiply page <br/>  n1={n1},n2={n2} and sum={n3}")


def modfun(request):
    n1 = 10
    n2 = 20
    n3 = n1 % n2
    return HttpResponse(f"<em>Modulo page</em> <br/>  n1={n1},n2={n2} and sum={n3}")
