"""Admin config for Jajio's Custom User"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin,
)
from django.utils.translation import ugettext_lazy as _

from improved_user.forms import (
    UserChangeForm,
    UserCreationForm,
)

from user.models import Address

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    """Admin panel for Improved User, mimics Django's default"""

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("full_name", "short_name", "type", "verified")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important dates"),
            {"fields": ("last_login", "date_joined")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "short_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = (
        "email",
        "full_name",
        "short_name",
        "is_staff",
        "type",
        "verified",
    )
    search_fields = ("email", "full_name", "short_name")
    ordering = ("email",)


admin.site.register(User, UserAdmin)

admin.site.register(Address)
