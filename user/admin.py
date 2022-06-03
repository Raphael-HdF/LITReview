from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

from .models import User


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'first_name',)
    list_filter = ('email', 'username', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'first_name', 'is_active', 'is_staff')
    fieldsets = (
        ('Login', {'fields': ('email', 'username', 'password',)}),
        ('Personal', {'fields': ('first_name', 'last_name', 'description')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )
    formfield_overrides = {
        User.description: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'password1', 'password2',
                'first_name', 'last_name', 'description', 'is_active',
                'is_staff')
        }
         ),
    )


admin.site.register(User, UserAdminConfig)
