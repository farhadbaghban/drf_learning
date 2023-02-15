from rest_framework.views import APIView
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from .models import Person, Question, Answer
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from permissions import IsOwnerOrReadOnly


class HomeView(APIView):
    """
    first step : without query_params

    secend : with query params

    third : recieve data with body

    fourth : using Serializer
    """

    # def get(self, request, *args, **kwargs):
    #     # return Response({"name": "farhad"})
    #     # name = request.GET["name"]
    #     name = request.query_params["name"]
    #     return Response({"name": name})

    # def post(self, request, *args, **kwargs):
    #     name = request.data["name"]
    #     return Response({"name": name})
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, requset, *args, **kwargs):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)


class QuestionListView(APIView):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    def post(self, request, *args, **kwargs):
        ser_data = QuestionSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [
        IsOwnerOrReadOnly,
    ]

    def put(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs["pk"])
        self.check_object_permissions(request, question)
        ser_data = QuestionSerializer(
            instance=question, data=request.POST, partial=True
        )
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs["pk"])
        question.delete()
        return Response({"message": "question deleted"}, status=status.HTTP_200_OK)
