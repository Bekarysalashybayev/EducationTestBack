from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from oauth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'is_active', 'first_name', 'last_name', 'middle_name', 'role')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'is_active', 'first_name', 'last_name', 'middle_name', 'role')
