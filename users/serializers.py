from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import User
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
    
    def update(self, instance: User, validated_data: dict):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.birthdate = validated_data.get("birthdate", instance.birthdate)
        instance.is_employee = validated_data.get("is_employee", instance.is_employee)
        instance.is_superuser = validated_data.get("is_employee", instance.is_employee)
        instance.password = validated_data.get("password", instance.password)
        
        instance.save()
        
        return instance


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        
        return token
