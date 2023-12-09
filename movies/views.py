from rest_framework.views import APIView, Request, Response, status
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Movie
from rest_framework.pagination import PageNumberPagination
from .permission import IsAdminOrReadOnly

# Create your views here.

class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
    def post(self, request: Request) -> Response:
        user = request.user
        serialized_movie = MovieSerializer(data=request.data, context={'user': user})
        serialized_movie.is_valid(raise_exception=True)
        serialized_movie.save()
        return Response(serialized_movie.data, status=status.HTTP_201_CREATED)


    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request)
        serializer_movies = MovieSerializer(result_page, many=True)
        return Response(serializer_movies.data)


class MovieByIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request: Request, movie_id) -> Response:
        try: 
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)
        serializer_movie = MovieSerializer(movie)
        return Response(serializer_movie.data)
    
    
    def delete(self, request: Request, movie_id) -> Response:
        try: 
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
