from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q
from .models import Recipe
from .serializers import RecipeSerializer
from .permissions import IsOwnerOrReadOnly

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.select_related("created_by").all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        ingredient = self.request.query_params.get("ingredient")
        category = self.request.query_params.get("category")
        if ingredient:
            # match ingredient anywhere in the free text (case-insensitive)
            qs = qs.filter(ingredients__icontains=ingredient)
        if category:
            qs = qs.filter(category__iexact=category)
        return qs

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
