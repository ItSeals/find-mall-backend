from rest_framework import serializers
from .models import Mall, Categories, Item

class MallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall
        fields = ["title", "description", "status", "created_at", "updated_at"]


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["title", "description", "status", "created_at", "updated_at"]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["title", "description", "status","category", "created_at", "updated_at"]