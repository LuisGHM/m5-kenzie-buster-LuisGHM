from rest_framework import serializers
from .models import RatingOpt, Movies

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(required=False)
    rating = serializers.ChoiceField(choices=RatingOpt, required=False)
    synopsis = serializers.CharField(required=False)
    added_by = serializers.CharField(required=False)
    
    def create(self, validated_data):
        new_movie = Movies.objects.create(**validated_data, user=self.context['user'])
        validated_data = new_movie
        validated_data.added_by = self.context['user'].email
        validated_data.save()
        return validated_data

