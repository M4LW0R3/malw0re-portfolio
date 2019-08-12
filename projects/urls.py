from django.urls import path
from . import views
urlpatterns = [
    path('', views.project_showcase, name="project_show"),
    path('<int:pk>/', views.project_detail, name="project_detail"),
]