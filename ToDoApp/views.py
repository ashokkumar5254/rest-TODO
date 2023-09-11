from django.shortcuts import render
from rest_framework.response import Response
from .models import todo_model
from .serializers import todo_serializer
# Create your views here.
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView

class fetching(ListAPIView):
    queryset=todo_model.objects.all()
    serializer_class=todo_serializer

class creating(CreateAPIView):
    queryset=todo_model.objects.all()
    serializer_class=todo_serializer

class updating(RetrieveUpdateAPIView):
    queryset=todo_model.objects.all()
    serializer_class=todo_serializer

class deleting(DestroyAPIView):
    queryset=todo_model.objects.all()
    serializer_class=todo_serializer
