from django.shortcuts import render
from .models import Books
from .serializers import BooksSerializers
from django.views.generic import ListView
from rest_framework import generics
# Create your views here.


class BooksView(ListView):
    def get(self, request):
        context = {}
        clay = Books.objects.all()
        context['data'] = clay
        return render(request, 'home/home.html', context)


class BooksSerializersView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
