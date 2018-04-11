from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return HttpResponse(u"django很有趣!")


def home(request):
    return render(request, 'home.html')


def add(request):
    # request.GET.get('a', 0)
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def addRest(request, a, b):
    c = int(a) + int(b);
    return HttpResponse(str(c))

# 转发
def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )
