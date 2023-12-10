from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['username'] = User.generate_username()
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'birthdate', 'biography', 'city', 'sex')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'birthdate', 'biography', 'city', 'sex')
