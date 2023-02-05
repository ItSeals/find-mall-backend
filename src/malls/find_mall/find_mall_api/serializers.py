from rest_framework import serializers
from .models import Mall, Categories, Item, Tag
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class MallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall
        fields = ["id", "title", "location"]


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["id", "title"]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "title", "item_image",  "category", "malls", "tags", "created_at", "updated_at"]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "title"]