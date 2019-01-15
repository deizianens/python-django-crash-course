from django.urls import path
from . import views

urlpatterns = [
    # from posts page, load views.py index
    path('', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
]
