from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Users
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserRegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is None: 
            return Response({'error' : 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh' : str(refresh),
            'access' : str(refresh.access_token)
        }, status=status.HTTP_200_OK)
    
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message" : "Logged Out Successfully!"},
                status=status.HTTP_205_RESET_CONTENT
                )
        
        except Exception:
            return Response(
                {"error" : 'Invalid or Expired refresh token.'},
                status=status.HTTP_400_BAD_REQUEST
            )
    
# For testing
class HomeView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response({'get message' : 'This is get request, accessed by all the user.'})
    
    def post(self, request):
        return Response({'Post message' : 'This Post request, Accessed by only authorized user.'})

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request):
        try:
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error" : "Invalid User."}, status=status.HTTP_400_BAD_REQUEST)
