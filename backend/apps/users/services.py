from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class AuthenticationService:
    @staticmethod
    def create_user(validated_data):
        password = validated_data.pop("password")

        user = User.objects.create_user(
            password=password,
            **validated_data,
        )

        return user

    @staticmethod
    def generate_tokens(user):
        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }