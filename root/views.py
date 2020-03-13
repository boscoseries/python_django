
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.throttling import UserRateThrottle
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

class OncePerDayUser(UserRateThrottle):
  rate = '2/day'

# @api_view(['GET', 'POST'])
# @throttle_classes([OncePerDayUser])
# def test(request):
#     return Response({'status': status.HTTP_200_OK})

@api_view(['GET', 'POST'])
def test(request):
    print(request.authenticators)
    print(request.auth)
    if request.method == 'POST':
        return Response({"message": request.data, "status": status.HTTP_201_CREATED})
    return Response({"message": "Hello, world!", "status": status.HTTP_200_OK})


class Test2(APIView):

  def get(self, request):
    print(request)
    return Response(data="This is a class based view", status=status.HTTP_200_OK)

  def post(self, request):
    return Response(data = request.data, status=status.HTTP_201_CREATED)

