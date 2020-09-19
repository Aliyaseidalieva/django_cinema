from rest_framework import generics

from .serializers import CreateRatingSerializer
from apps.movies.service import get_client_ip


class AddStarRatingView(generics.CreateAPIView):
    """Добавление рейтинга фильму"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))
