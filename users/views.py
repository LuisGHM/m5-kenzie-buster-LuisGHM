from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwner

# Create your views here.
class UserView(APIView):
    
    def post(self, request: Request) -> Response:
        serialized_user = UserSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response(serialized_user.data, status=status.HTTP_201_CREATED)

class UserByIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get(self, request: Request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        user_serialized = UserSerializer(user)
        
        return Response(user_serialized.data)


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

        