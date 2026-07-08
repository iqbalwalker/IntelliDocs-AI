from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class AuthenticationService:
    @staticmethod
    def create_user(validated_data):
        email = validated_data["email"]

        if User.objects.filter(email=email).exists():
            raise ValidationError(
                {"email": ["A user with this email already exists."]}
            )

        password = validated_data.pop("password")

        user = User.objects.create_user(
            password=password,
            **validated_data,
        )

        return user

    @staticmethod
    def login(email, password):
        user = authenticate(
            username=email,
            password=password,
        )

        if user is None:
            raise ValidationError(
                {"detail": ["Invalid email or password."]}
            )

        return user

    @staticmethod
    def generate_tokens(user):
        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }