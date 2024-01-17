from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return HttpResponse("Hello, Django!")

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

