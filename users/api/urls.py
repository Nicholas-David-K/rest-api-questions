from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('users', views.CustomUserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginAPIView.as_view(), name='login-view')
]