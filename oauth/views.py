from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from oauth.models import User
from oauth.serializers import ProfileSerializer, RegistrationSerializer


class ProfileInfoVIew(RetrieveAPIView):
    """ Профиль инфо """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return user


class CreateStudentUserView(CreateAPIView):
    """ Регистрация """
    serializer_class = RegistrationSerializer

    # def post(self, request, *args, **kwargs):
    #     username = self.request.data.get('username')
    #     if not username:
    #         return Response({'detail': 'Username required'},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #
    #     username = username.lower().strip()
    #     user = User.objects.filter(username=username)
    #
    #     if user.filter(is_active=True).exists():
    #         return Response({'detail': 'Такой пользователь уже существует'},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #     user_is_not_active = user.filter(is_active=False)
    #     if user_is_not_active.exists():
    #         user_is_not_active.delete()
    #     return self.create(request, *args, **kwargs)
