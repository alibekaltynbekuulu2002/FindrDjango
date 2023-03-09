from .models import User
from rest_framework import generics
from .serializers import UserSerializer


class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserGetApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserUpdateApiView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserDeleteApiView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

