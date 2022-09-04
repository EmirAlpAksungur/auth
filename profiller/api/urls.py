from django.urls import path, include

from profiller.api.view import ProfileListAPIView,ProfileStateListAPIView,ProfileIdListAPIView


urlpatterns = [
    path('', ProfileListAPIView.as_view(),name='list'),
    path('<int:pk>', ProfileIdListAPIView.as_view(),name='profile'),
    path('durum/<int:pk>', ProfileStateListAPIView.as_view(),name='profile-state'),
]