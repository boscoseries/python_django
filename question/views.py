from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from question.models import Question
from question.serializers import QuestionSerializer


class QuestionView(APIView):
    def get_questions(self):
        try:
            return Question.objects.all()
        except Question.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST

    def get(self, request, format=None):
        queryset = self.get_questions()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
