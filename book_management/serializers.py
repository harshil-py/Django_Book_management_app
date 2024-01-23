from rest_framework import serializers
from book_management.models import *

class AuthorEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorEntity
        fields = "__all__"

class BookEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookEntity
        fields = "__all__"