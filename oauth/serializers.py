from rest_framework import serializers

from core.constants.RoleChoices import ROLES
from oauth.models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    """ Роль Serializer """

    class Meta:
        model = Role
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    """ Профиль Serializer """

    role = RoleSerializer()

    class Meta:
        model = User
        fields = ('username', 'role', 'first_name', 'last_name',)


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Creates a new user.
    Email, username, and password are required.
    Returns a JSON web token.
    """

    # The password must be validated and should not be read by the client
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'password')

    def create(self, validated_data):
        role = Role.objects.filter(name=ROLES.STUDENT).first()
        validated_data['role'] = role
        return User.objects.create_user(**validated_data)
