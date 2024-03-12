from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("category/<slug:slug>", views.CategoryDetailView.as_view(), name="category_detail"),
]