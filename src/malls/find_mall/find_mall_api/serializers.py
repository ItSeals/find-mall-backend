from rest_framework import serializers
from .models import Mall, Categories, Item, Tag

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
        fields = ["id", "title", "category", "malls", "tags", "created_at", "updated_at"]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "title"]