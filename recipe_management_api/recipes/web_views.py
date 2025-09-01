
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib import messages
from django.shortcuts import redirect
from .models import Recipe
from django.db.models import Q

class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.created_by == self.request.user

class RecipeDashboardView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/dashboard.html"
    context_object_name = "recipes"
    paginate_by = 10

    def get_queryset(self):
        qs = Recipe.objects.filter(created_by=self.request.user).order_by("-created_at")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(ingredients__icontains=q) | Q(category__icontains=q))
        return qs

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ["title", "category", "ingredients", "steps", "description", 'image']
    template_name = "recipes/form.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Recipe created successfully.")
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Recipe
    fields = ["title", "category", "ingredients", "steps", "description", 'image']
    template_name = "recipes/form.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        messages.success(self.request, "Recipe updated successfully.")
        return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/confirm_delete.html"
    success_url = reverse_lazy("dashboard")

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, "Recipe deleted.")
        return super().delete(request, *args, **kwargs)

# Section pages

class SectionShowAllView(RecipeDashboardView):
    template_name = "recipes/section_show_all.html"

class SectionAddView(RecipeCreateView):
    template_name = "recipes/section_add.html"

class SectionDeleteListView(RecipeDashboardView):
    template_name = "recipes/section_delete.html"

class SectionModifyRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False
    def get_redirect_url(self, *args, **kwargs):
        # Send users to the main dashboard where they can click 'Edit' on any row
        return reverse_lazy("dashboard")
