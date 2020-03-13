from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import Person
from user.serializers import PersonSerializer


class PersonView(APIView):

    def get_persons(self):
        try:
            return Person.objects.all()
        except Person.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST

    def get(self, request, format=None):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
