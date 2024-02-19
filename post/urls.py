from django.urls import path
from post import views

urlpatterns = [
    path('', views.MainPostAPIView.as_view()),
    path('category/', views.CategoryListAPIView.as_view()),
    path('detail/<int:pk>/', views.PostDetailRetrieveAPIView.as_view()),
]