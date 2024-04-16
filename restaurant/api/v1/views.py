from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

from menu.models import Food, FoodCategory

from .serializers import FoodListSerializer


class FoodCategoryListView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        subquery = Food.objects.filter(is_publish=True)
        prefetch = Prefetch('food', queryset=subquery)
        return FoodCategory.objects.filter(
            food__is_publish=True
        ).distinct().prefetch_related(prefetch).order_by('id')
