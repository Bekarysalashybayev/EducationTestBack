from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from oauth.forms import CustomUserChangeForm, CustomUserCreationForm
from oauth.models import Role, User


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name"]


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = [
#         "username", 'first_name', 'last_name', "is_superuser", "role", "created", "modified",
#     ]
#     search_fields = ["user_id", "username"]
#     list_filter = ['role']


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('id', 'username', 'first_name', 'last_name', 'role', 'is_active',)
    fieldsets = (
        ("User data", {'fields': ('username', 'first_name', 'last_name', 'middle_name', 'role', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        ("User data", {
            'classes': ('wide',),
            'fields': (
                'username', 'first_name', 'last_name', 'middle_name', 'role', 'password1', 'password2')}
         ),
        ('Permissions', {'fields': ('is_superuser', 'is_active')}),
    )
    search_fields = ('id', 'username',)


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
