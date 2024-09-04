from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# GET, POST
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# PUT - изменение записи
class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# DELETE
class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
