from django.urls import path

from api.v1.views import FoodCategoryListView

urlpatterns = [
    path('foods/', FoodCategoryListView.as_view(), name='foods'),
]
