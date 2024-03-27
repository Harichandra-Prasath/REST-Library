from rest_framework import serializers
from .models import Book,Library

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('ISBN','Title','Author','Publication_Date','Description')

