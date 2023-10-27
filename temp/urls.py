from django.urls import path
from .views import BooksView, BooksSerializersView

urlpatterns = [
    path('', BooksView.as_view(), name='home'),
    path('all-books', BooksSerializersView.as_view()),
]