from rest_framework import serializers
from rest_framework_jwt.serializers import User

from project.mauth.models import Profile


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(read_only=True, source="user.username")

    class Meta:
        model = Profile
        fields = ('id', 'phone', 'point_amount', 'user_name', 'first_name', 'last_name', 'email', 'photo')
