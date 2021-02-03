from .serializers import CustomUserSerializer
from rest_framework import viewsets
from users.models import CustomUser
from .permissions import IsOwnerOrReadOnly

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]



class UserLoginAPIView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


