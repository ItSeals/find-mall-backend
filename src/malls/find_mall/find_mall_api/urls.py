from django.urls import path, include
from .views import (
    MallListApiView,
    MallDetailApiView,
)

urlpatterns = [
    path('mall/', MallListApiView.as_view()),
    path('mall/<int:mall_id>/', MallDetailApiView.as_view())
]
