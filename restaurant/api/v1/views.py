from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

from menu.models import Food, FoodCategory

from .serializers import FoodListSerializer


class FoodCategoryListView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        subquery = Food.objects.filter(is_publish=True)
        return FoodCategory.objects.exclude(food=None).prefetch_related(
            Prefetch('food', queryset=subquery)
        ).order_by('id')
