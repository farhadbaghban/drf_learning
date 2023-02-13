from rest_framework.views import APIView
from django.contrib import messages
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer


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

    def get(self, requset, *args, **kwargs):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)
