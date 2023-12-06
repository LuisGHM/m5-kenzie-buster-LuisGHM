from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class UserView(APIView):
    
    def post(self, request: Request) -> Response:
        serialized_user = UserSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response(serialized_user.data, status=status.HTTP_201_CREATED)


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

        