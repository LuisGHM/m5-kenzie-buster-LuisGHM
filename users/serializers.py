from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField()
    is_employee = serializers.BooleanField()
    is_superuser = serializers.BooleanField(read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        email = validated_data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("email already registered.")

        username = validated_data.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("username already taken.")

        user = User.objects.create(**validated_data)
        return user
