from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate

from django.shortcuts import render

class UserLogin(APIView):
    
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh_token = RefreshToken.for_user(user)
            access_token = str(refresh_token.access_token)
            context = {
                'message': 'Logged in successfully',
                'token': access_token
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


def index(request):
    return render(request, 'account/index.html')