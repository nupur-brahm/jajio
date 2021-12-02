from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django_registration.validators import (
    DUPLICATE_EMAIL,
    CaseInsensitiveUnique,
    validate_confusables_email,
)
from django.forms import ModelForm
User = get_user_model()


class RegistrationForm(UserCreationForm):
    """Form for registering a new user account.

    Validates that the requested email is not already in use, and
    requires the password to be entered twice to catch typos.
    """

    class Meta:
        model = User
        fields = [
            User.USERNAME_FIELD,
            "password1",
            "password2",
            "full_name",
            "short_name",
        ]
        field_classes = {}

    error_css_class = "error"
    required_css_class = "required"

    def __init__(self, *args, **kwargs):
        """Configure username/email field to be validated"""
        super().__init__(*args, **kwargs)
        self.fields[User.USERNAME_FIELD].validators.extend(
            [
                validate_confusables_email,
                CaseInsensitiveUnique(
                    User,
                    User.USERNAME_FIELD,
                    DUPLICATE_EMAIL,
                ),
            ]
        )

class CompanyRegistrationForm(UserCreationForm):
    """Form for registering a new company account.

    Validates that the requested email is not already in use, and
    requires the password to be entered twice to catch typos.
    """

    class Meta:
        model = User
        fields = [
            User.USERNAME_FIELD,
            "password1",
            "password2",
            "full_name",
            "short_name",
        ]
        field_classes = {}

    error_css_class = "error"
    required_css_class = "required"

    def __init__(self, *args, **kwargs):
        """Configure username/email field to be validated"""
        super().__init__(*args, **kwargs)
        self.fields[User.USERNAME_FIELD].validators.extend(
            [
                validate_confusables_email,
                CaseInsensitiveUnique(
                    User,
                    User.USERNAME_FIELD,
                    DUPLICATE_EMAIL,
                ),
            ]
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.type = "company"
        user.verified = False
        if commit:
            user.save()
        return user


class CompanyApproveForm(ModelForm):
    
    class Meta:
        model = User
        fields = ["verified"]
    