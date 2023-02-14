from rest_framework import serializers
from django.contrib.auth.models import User


def clean_email(value):
    if "admin" in value:
        raise serializers.ValidationError("you cant use admin in email")


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("password must be match")
        return data

    def validate_username(self, value):
        if value == "admin":
            raise serializers.ValidationError("you cant use admin")
        return value
