from django.urls import path, include, re_path
from .views import (
    UserSignUp,
    UserLogin,
    MallListApiView,
    MallDetailApiView,
    CategoriesListApiView,
    CategoriesDetailApiView,
    ItemsListApiView,
    ItemsDetailApiView,
    ItemParameterApiView,
    TagListApiView,
    TagDetailApiView,
    OtherTagListApiView,
    OtherTagDetailApiView
)

urlpatterns = [
    path('signin', UserLogin.as_view()),
    path('signup', UserSignUp.as_view()),
    path('mall', MallListApiView.as_view()),
    path('mall/<int:mall_id>', MallDetailApiView.as_view()),
    path('category', CategoriesListApiView.as_view()),
    path('category/<int:category_id>', CategoriesDetailApiView.as_view()),
    path('item/<int:item_id>', ItemsDetailApiView.as_view()),
    re_path(r'^item$', ItemsListApiView.as_view()),
    re_path(r'^item(?:category_id=(?P<category_id>\d+))?', ItemParameterApiView.as_view()),
    re_path(r'^item(?:search=(?P<search>\D+))?', ItemParameterApiView.as_view()),
    re_path(r'^item(?:search=(?P<search>\D+)&mall_ids=(?P<mall_ids>\D+)&category_ids=(?P<category_ids>\D+)&tag_ids=(?P<tag_ids>\D+))?'
    , ItemParameterApiView.as_view()),
    #re_path(r'^item(?:tag_name=(?P<tag_name>\D+))?', ItemParameterApiView.as_view()),
    path('tag', TagListApiView.as_view()),
    path('tag/<int:tag_id>', TagDetailApiView.as_view()),
    path('othertag', OtherTagListApiView.as_view()),
    path('othertag/<int:OtherTag_id>', OtherTagDetailApiView.as_view())
]
