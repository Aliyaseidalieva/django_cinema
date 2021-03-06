from rest_framework.generics import ListAPIView

from .serializers import CategorySerializer
from .models import Category


class CategoryListAPIView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()