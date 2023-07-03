from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)


urlpatterns = [
    path('', include(router.urls),),
    path('questions/<int:pk>/answer-question/', views.AnswerCreateAPIView.as_view(), name='answer-create'),

    path('answers/<int:pk>/', views.AnswerRetrieveUpdateDestroyAPIView.as_view(), name='answer-detail'),

    path('answers/<int:pk>/like/', views.AnswerLikeAPIView.as_view(), name='answer-like'),

    path('questions/<int:pk>/answers/', views.AnswerListAPIView.as_view(), name='answer-list'),
]