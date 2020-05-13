from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def index(request):
    return HttpResponse('aaaaaaaaaa')


class IndexView(TemplateView):
    template_name = 'app01/index.html'

