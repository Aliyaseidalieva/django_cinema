from django.urls import path
from . import views


urlpatterns = [
    path('', views.AddStarRatingView.as_view(), name='rating'),
]