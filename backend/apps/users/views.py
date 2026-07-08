from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import(
    RegisterSerializer,
    UserSerializer,
)

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class ProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user