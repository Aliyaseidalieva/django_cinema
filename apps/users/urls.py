from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserProfileListCreateView.as_view(), name='all-profiles'),
    path('profile/<int:pk>', views.userProfileDetailView.as_view(), name='profile'),
]