from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_client/', views.add_client, name="add_client"),
    path('add_relation/', views.add_relation, name="add_relation"),
    path('check_relation/', views.check_relation, name="check_relation")
]
