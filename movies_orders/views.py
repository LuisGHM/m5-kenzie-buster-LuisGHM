from rest_framework.views import APIView, Request, Response, status
from .serializers import MovieOrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request: Request, movie_id) -> Response:
        user = request.user
        serialized_movie_order = MovieOrderSerializer(data=request.data, context={"user": user, "movie_id": movie_id})
        serialized_movie_order.is_valid(raise_exception=True)
        serialized_movie_order.save()
        return Response(serialized_movie_order.data, status=status.HTTP_201_CREATED)
        