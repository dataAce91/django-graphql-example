from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import viewsets
from . serializers import BookSerializers
from . models import Books
# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('bookID')
    serializer_class = BookSerializers

def getbooks(request):
    return HttpResponse("This is get books page")

