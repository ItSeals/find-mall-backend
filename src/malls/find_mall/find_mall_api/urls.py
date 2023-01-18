from django.urls import path, include, re_path
from .views import (
    MallListApiView,
    MallDetailApiView,
    CategoriesListApiView,
    CategoriesDetailApiView,
    ItemsListApiView,
    ItemsDetailApiView,
    ItemCategoryApiView,
    ItemSearchApiView,
    TagListApiView,
    TagDetailApiView
)

urlpatterns = [
    path('mall', MallListApiView.as_view()),
    path('mall/<int:mall_id>', MallDetailApiView.as_view()),
    path('category', CategoriesListApiView.as_view()),
    path('category/<int:category_id>', CategoriesDetailApiView.as_view()),
    path('item', ItemsListApiView.as_view()),
    #path('item/<int:item_id>', ItemsDetailApiView.as_view()),
    re_path(r'^item/(?P<item_id>\d+)', ItemsDetailApiView.as_view()),
    re_path(r'^item/(?P<category_id>\d+)', ItemsDetailApiView.as_view()),
    re_path(r'^item/(?P<item_name>\D+)', ItemsDetailApiView.as_view()),
    re_path(r'^item/(?P<tag_name>\D+)', ItemsDetailApiView.as_view()),
    #path('items/<int:category_id>', ItemCategoryApiView.as_view()),
    #path('items/search/<name>', ItemSearchApiView.as_view()),
    path('tag', TagListApiView.as_view()),
    path('tag/<int:tag_id>', TagDetailApiView.as_view()),
]
