from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
path("admin/", admin.site.urls),
path("", RedirectView.as_view(pattern_name="dashboard", permanent=False)),
path("accounts/", include("accounts.urls")),
path("academics/", include("academics.urls")),
path("api-auth/", include("rest_framework.urls")),
]