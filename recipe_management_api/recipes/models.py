from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField(help_text="One or more ingredients; free text")
    steps = models.TextField(help_text="Recipe steps; free text")
    category = models.CharField(max_length=100, db_index=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
