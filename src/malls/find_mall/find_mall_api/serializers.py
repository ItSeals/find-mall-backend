from rest_framework import serializers
from .models import Mall, Categories, Item

class MallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall
        fields = ["title", "location"]


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["title"]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["title", "category", "malls", "created_at", "updated_at"]