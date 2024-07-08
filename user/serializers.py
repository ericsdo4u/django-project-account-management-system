from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseCreateSerializer
from user.models import User


class UserCreateSerializer(BaseCreateSerializer):
    class Meta(BaseCreateSerializer.Meta):

        fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'password']
