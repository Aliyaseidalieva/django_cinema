from django.urls import path
from . import views


urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie-list'),
    path('upload/', views.FileUploadView.as_view()),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('actors/', views.ActorsListView.as_view(), name='actor-list'),
    path('actors/<int:pk>/', views.ActorsDetailView.as_view(), name='actor-detail'),
    path('reviews/', views.ReviewCreateView.as_view(), name='reviews'),
]