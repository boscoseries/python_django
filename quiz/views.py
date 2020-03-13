from django.shortcuts import render
from quiz.serializers import QuizSerializer
from quiz.models import Quiz
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class QuizView(APIView):

	def get_quizes(self):
			try:
					return Quiz.objects.all()
			except Quiz.DoesNotExist:
					raise status.HTTP_404_NOT_FOUND

	def get(self, request, format=None):
			queryset = self.get_quizes()
			serializer = QuizSerializer(queryset, many=True)
			return Response(data=serializer.data, status=status.HTTP_201_CREATED)

	def post(self, request):
			serializer = QuizSerializer(data=request.data)
			try:
					if serializer.is_valid():
							serializer.save()
							return Response(serializer.data, status=status.HTTP_201_CREATED)
			except Exception as e:
				return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
