from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField()
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        errors = {}

        if email and User.objects.filter(email=email).exists():
            errors['email'] = 'Email already registered.'

        if username and User.objects.filter(username=username).exists():
            errors['username'] = 'Username already taken.'

        if errors:
            raise ValidationError(errors)

        return data

    def create(self, validated_data):
        if validated_data["is_employee"] is False:
            user = User.objects.create_user(**validated_data)
        else:
            user = User.objects.create_superuser(**validated_data)

        return user
