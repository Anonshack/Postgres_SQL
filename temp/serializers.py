from rest_framework import serializers
from .models import Books


class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'name', 'year', 'info']