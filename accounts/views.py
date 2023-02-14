from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status

# from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserRegisterSerializer

# create method Overwrited
class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            user = ser_data.create(ser_data.validated_data)
            Token.objects.create(user=user)
            # User.objects.create_user(
            #     username=ser_data.validated_data["username"],
            #     email=ser_data.validated_data["email"],
            #     password=ser_data.validated_data["password"],
            # )
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
