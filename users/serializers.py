import uuid

from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        username = uuid.uuid4().hex[:6].upper()
        validated_data['username'] = username
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'birthdate', 'biography', 'city', 'sex')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'birthdate', 'biography', 'city', 'sex')
