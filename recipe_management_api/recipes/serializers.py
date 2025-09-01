from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Recipe
        fields = ["id","title","description","ingredients","steps","category","created_by","created_at", 'image']
        read_only_fields = ["id","created_by","created_at", 'image']
