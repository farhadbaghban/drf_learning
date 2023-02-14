from rest_framework import serializers
from django.contrib.auth.models import User


"""
    first = strat serializer

    second = user model serializer
    third = overwrite create
"""


def clean_email(value):
    if "admin" in value:
        raise serializers.ValidationError("you cant use admin in email")


# class UserRegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     email = serializers.EmailField(required=True, validators=[clean_email])
#     password = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")
        extra_kwargs = {
            "email": {"validators": [clean_email]},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        del validated_data["password2"]
        return User.objects.create_user(**validated_data)

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("password must be match")
        return data

    def validate_username(self, value):
        if value == "admin":
            raise serializers.ValidationError("you cant use admin")
        return value
