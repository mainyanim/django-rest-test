from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework import viewsets
from .models import Items
from .serializers import ItemsSerializer
# Create your views here.
def index (request):
    return HttpResponse("It works!")

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
