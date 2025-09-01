from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib.auth import views as auth_views
from users.web_views import SignUpView
from recipes.web_views import (
    RecipeDashboardView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView,
    SectionShowAllView, SectionAddView, SectionModifyRedirectView, SectionDeleteListView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(pattern_name="login_form", permanent=False), name="home"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login_form"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/register/", SignUpView.as_view(), name="register_form"),
    path("dashboard/", RecipeDashboardView.as_view(), name="dashboard"),
    path("recipes/new/", RecipeCreateView.as_view(), name="recipe_create"),
    path("recipes/<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("recipes/<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("dashboard/show-all/", SectionShowAllView.as_view(), name="dashboard_show_all"),
    path("dashboard/add/", SectionAddView.as_view(), name="dashboard_add"),
    path("dashboard/modify/", SectionModifyRedirectView.as_view(), name="dashboard_modify"),
    path("dashboard/delete/", SectionDeleteListView.as_view(), name="dashboard_delete"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("", include("users.urls")),
    path("", include("recipes.urls")),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
