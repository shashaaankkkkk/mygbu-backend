from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone', 'user_type']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            user_type=validated_data['user_type'],
            password_hash=make_password(password)
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        if not check_password(data['password'], user.password_hash):
            raise serializers.ValidationError("Invalid credentials")

        return user
