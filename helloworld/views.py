from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
  with open('config/app.config', 'r') as fh:
      config=fh.read()
  return HttpResponse("Hello, World!         " + config + "\n")
