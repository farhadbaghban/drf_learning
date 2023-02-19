# from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserRegisterSerializer, UserViewSetSerializer

"""
    using viewsets
"""


class UserViewSet(viewsets.ViewSet):
    query_set = User.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def list(self, request):
        ser_data = UserViewSetSerializer(instance=self.query_set, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.query_set, pk=pk)
        ser_data = UserViewSetSerializer(instance=user)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            user = ser_data.create(ser_data.validated_data)
            Token.objects.create(user=user)
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.query_set, pk=pk)
        if user != request.user:
            return Response(
                {"message": "Permission Denied. you are Not Owner"},
                status=status.HTTP_403_FORBIDDEN,
            )
        ser_data = UserViewSetSerializer(instance=user, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.query_set, pk=pk)
        if user != request.user:
            return Response(
                {"message": "Permission Denied. you are Not Owner"},
                status=status.HTTP_403_FORBIDDEN,
            )
        user.is_active = False
        user.save()
        return Response({"message": "user DeActivated"}, status=status.HTTP_200_OK)


# # create method Overwrited
# class UserRegisterView(APIView):
#     def post(self, request, *args, **kwargs):
#         ser_data = UserRegisterSerializer(data=request.POST)
#         if ser_data.is_valid():
#             user = ser_data.create(ser_data.validated_data)
#             Token.objects.create(user=user)
#             # User.objects.create_user(
#             #     username=ser_data.validated_data["username"],
#             #     email=ser_data.validated_data["email"],
#             #     password=ser_data.validated_data["password"],
#             # )
#             return Response(ser_data.data, status=status.HTTP_201_CREATED)
#         return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
