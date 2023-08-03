from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response
from .services import getRecommendations
class UserViewSet(APIView):
    def post(self, request):
        res = getRecommendations(request.body)
        return Response(res)
