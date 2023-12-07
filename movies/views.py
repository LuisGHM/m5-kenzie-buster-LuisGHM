from rest_framework.views import APIView, Request, Response, status
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Movies

# Create your views here.

class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def post(self, request: Request) -> Response:
        user = request.user
        serialized_movie = MovieSerializer(data=request.data, context={'user': user})
        serialized_movie.is_valid(raise_exception=True)
        serialized_movie.save()
        return Response(serialized_movie.data, status=status.HTTP_201_CREATED)


    def get(self, request: Request) -> Response:
        movies = Movies.objects.all()
        serializer_movies = MovieSerializer(movies, many=True)
        return Response(serializer_movies.data)
