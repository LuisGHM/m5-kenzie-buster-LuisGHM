from rest_framework import serializers
from .models import MovieOrder
from movies.models import Movie

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    purchased_by = serializers.CharField(read_only=True)
    purchased_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    
    def create(self, validated_data):
        movie = Movie.objects.get(id=self.context["movie_id"])
        new_order_movie = MovieOrder.objects.create(**validated_data, movie=movie, user=self.context["user"])
        validated_data = new_order_movie
        validated_data.title = movie.title
        validated_data.purchased_by = self.context["user"].email
        return validated_data 
        
        