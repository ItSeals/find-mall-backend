from django.urls import path, include, re_path
from .views import (
    UserApiView,
    MallListApiView,
    MallDetailApiView,
    CategoriesListApiView,
    CategoriesDetailApiView,
    ItemsListApiView,
    ItemsDetailApiView,
    ItemParameterApiView,
    TagListApiView,
    TagDetailApiView
)

urlpatterns = [
    path('user', UserApiView.as_view()),
    path('mall', MallListApiView.as_view()),
    path('mall/<int:mall_id>', MallDetailApiView.as_view()),
    path('category', CategoriesListApiView.as_view()),
    path('category/<int:category_id>', CategoriesDetailApiView.as_view()),
    path('item/<int:item_id>', ItemsDetailApiView.as_view()),
    re_path(r'^item$', ItemsListApiView.as_view()),
    re_path(r'^item(?:category_id=(?P<category_id>\d+))?', ItemParameterApiView.as_view()),
    re_path(r'^item(?:search=(?P<search>\D+))?', ItemParameterApiView.as_view()),
    #re_path(r'^item(?:tag_name=(?P<tag_name>\D+))?', ItemParameterApiView.as_view()),
    path('tag', TagListApiView.as_view()),
    path('tag/<int:tag_id>', TagDetailApiView.as_view()),
]
