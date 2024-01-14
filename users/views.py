from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from users.serializers import RegisterSerializer, UserSerializer


class JWTLoginMixin:
    @staticmethod
    def response_jwt(user: User):
        refresh = RefreshToken.for_user(user)
        return Response(
            status=status.HTTP_200_OK,
            data={
                'id': user.id,
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
            }
        )


class RegisterView(JWTLoginMixin, CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return self.response_jwt(user)


class LoginView(JWTLoginMixin, CreateAPIView):
    def create(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=request.data.get('id'))
        if user.check_password(request.data.get('password')):
            return self.response_jwt(user)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSearchView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        first_name = self.request.GET.get('first_name')
        last_name = self.request.GET.get('last_name')
        qs = User.objects.all().order_by('id')
        if first_name:
            qs = qs.filter(first_name__startswith=first_name)
        if last_name:
            qs = qs.filter(last_name__startswith=last_name)
        # print(qs.explain())
        return qs
