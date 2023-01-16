from django.urls import path, include
from .views import (
    MallListApiView,
    MallDetailApiView,
    CategoriesListApiView,
    CategoriesDetailApiView,
    ItemsListApiView,
    ItemsDetailApiView,
    ItemCategoryApiView,
    ItemSearchApiView
)

urlpatterns = [
    path('mall/', MallListApiView.as_view()),
    path('mall/<int:mall_id>/', MallDetailApiView.as_view()),
    path('category/', CategoriesListApiView.as_view()),
    path('category/<int:category_id>/', CategoriesDetailApiView.as_view()),
    path('item/', ItemsListApiView.as_view()),
    path('item/<int:item_id>/', ItemsDetailApiView.as_view()),
    path('items/<int:category_id>/', ItemCategoryApiView.as_view()),
    path('items/search/<name>/', ItemSearchApiView.as_view())
]
