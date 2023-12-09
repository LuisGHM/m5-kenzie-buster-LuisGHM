from rest_framework import serializers
from .models import RatingOpt, Movie
from users.models import User
import pdb

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(allow_blank=True, required=False)
    rating = serializers.ChoiceField(choices=RatingOpt, required=False)
    synopsis = serializers.CharField(allow_blank=True, required=False)
    added_by = serializers.SerializerMethodField(required=False)
    
    def get_added_by(self, obj):
        user = User.objects.get(id=obj.user_id)
        added_by = user.email
        return added_by
        
    
    def create(self, validated_data):
        new_movie = Movie.objects.create(**validated_data, user=self.context['user'])
        validated_data = new_movie
        validated_data.added_by = self.context['user'].email
        validated_data.save()
        return validated_data

