from django.shortcuts import render
from rest_framework import generics
from .serializers import TankenListSerializer, TankenDetailSerializer
from .models import Tanken
from django.views.generic import ListView, DetailView, FormView
from django.views.generic import CreateView, UpdateView, TemplateView

class TankenListView(ListView):
    model = Tanken
    template_name = "tanklist.html"
    
class TankenCreateView(CreateView):
    model = Tanken
    template_name = "tanken_new.html"
    fields = ["datum", "betrag", "bemerkung"]

class TankenListAPIView(generics.ListAPIView):
    queryset = Tanken.objects.all()
    serializer_class = TankenListSerializer

class TankenRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Tanken.objects.all()
    serializer_class = TankenDetailSerializer

class TankenCreateAPIView(generics.CreateAPIView):
    queryset = Tanken.objects.all()
    serializer_class = TankenDetailSerializer

class TankenRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Tanken.objects.all()
    serializer_class = TankenDetailSerializer

class TankenDestroyAPIView(generics.DestroyAPIView):
    lookup_field ="id"
    queryset = Tanken.objects.all()