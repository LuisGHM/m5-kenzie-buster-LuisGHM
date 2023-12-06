from rest_framework import serializers
from .models import RatingOpt


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(required=False)
    rating = serializers.CharField(choices=RatingOpt, required=False)
    synopsis = serializers.CharField()
    added_by = serializers.CharField(read_only=True)
    