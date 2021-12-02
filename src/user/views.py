"""Views for User app"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    PasswordChangeView as BasePasswordChangeView,
    PasswordResetConfirmView as BasePasswordResetConfirmView,
    PasswordResetView as BasePasswordResetView,
)
from django.contrib.messages import success
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django_registration.backends.activation.views import (
    ActivationView as BaseActivationView,
)
from django_registration.exceptions import ActivationError

from .forms import CompanyApproveForm
from .models import User
from django.utils.translation import gettext_lazy as _

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
from .serializers import(
    CompanySerializer,
    BuyerSerializer,
)

from functools import reduce
from operator import or_
from .utils import get_perms
from django.contrib.auth.models import Permission



class AccountPage(LoginRequiredMixin, TemplateView):
    """Display page with links to manage account

    For instance, link to page to change password.
    """

    template_name = "user/account.html"


class ActivationView(BaseActivationView):
    """Notify user of activation and direct to login"""

    success_url = reverse_lazy("auth:login")
    NOT_VERIFIED_MESSAGE = _("The account has not been verfied by our administrators.")

    # def activate(self, *args, **kwargs):
    #     """Notify user after activating successfully

    #     https://github.com/ubernostrum/django-registration/blob/58be01f5858a/src/django_registration/backends/activation/views.py#L129
    #     """
    #     user = super().activate(*args, **kwargs)
    #     success(
    #         self.request,
    #         "Your account has been activated."
    #         " You may now sign-in.",
    #         fail_silently=True,
    #     )
    #     return user

    def activate(self, *args, **kwargs):
        username = self.validate_key(kwargs.get("activation_key"))
        user = self.get_user(username)
        if user.verified:
            user.is_active = True
            # add permissions if the user is company
            if user.type == 'company':
                user.user_permissions.add(
                    *list(
                        Permission.objects.filter(
                            reduce(
                                or_,
                                (
                                    get_perms(perms)
                                    for perms in [
                                        "core.add_item",
                                        "core.change_item",
                                        "core.delete_item",
                                        "core.view_item",
                                    ]
                                )
                            )
                        )
                    )
                )
            user.save()
            success(
                self.request,
                "Your account has been activated."
                " You may now sign-in.",
                fail_silently=True,  
            )
            return user
        else:
            raise ActivationError(
                self.NOT_VERIFIED_MESSAGE, code="not_verified"
            )


class SuccessMessageMixin:
    """Notify user of success after submitting a form"""

    success_message = "Success!"

    def form_valid(self, form):
        """When form is valid: notify user of success"""
        success(
            self.request,
            self.success_message,
            fail_silently=True,
        )
        return super().form_valid(form)


class PasswordChangeView(
    SuccessMessageMixin, BasePasswordChangeView
):
    """Allow authenticated users to change password;

    Messages success to user
    """

    success_message = "Password Changed Successfully"
    success_url = reverse_lazy("auth:account")
    template_name = "user/password_change_form.html"


class PasswordResetView(
    SuccessMessageMixin, BasePasswordResetView
):
    """Allow anonymous users to reset password;

    Messages success to user
    """

    email_template_name = "user/password_reset_email.txt"
    subject_template_name = (
        "user/password_reset_subject.txt"
    )
    success_message = (
        "Password email sent: please check your email"
    )
    success_url = reverse_lazy("auth:login")
    template_name = "user/password_reset_form.html"


class PasswordResetConfirmView(
    SuccessMessageMixin, BasePasswordResetConfirmView
):
    """Prompt user for a new password"""

    success_message = "Password reset: Please login with your new password."
    success_url = reverse_lazy("auth:login")
    template_name = "user/password_reset_confirm.html"

class CompanyApprovalPendingList(ListView):

    queryset = User.objects.all().filter(verified=False)
    template_name = 'user/company_pending_approval.html'

class CompanyApproveView(UpdateView):
    
    success_url = reverse_lazy("auth:django_approval_pending_companies")
    form_class = CompanyApproveForm
    queryset = User.objects.all()
    template_name = "user/approve_company.html"


class UserList(ListView):
    queryset = User.objects.all()
    template_name = 'user/list.html'


# API views
class CompanyApiDetail(RetrieveAPIView):
    queryset = User.objects.all().filter(type='company', is_staff=False)
    serializer_class = CompanySerializer
    lookup_field = "uid"

class CompanyApiList(ListAPIView):

    queryset = User.objects.all().filter(type='company', is_staff=False)
    serializer_class = CompanySerializer


class BuyerApiDetail(RetrieveAPIView):
    queryset = User.objects.all().filter(type='buyer', is_staff=False)
    serializer_class = CompanySerializer
    lookup_field = "uid"

class BuyerApiList(ListAPIView):

    queryset = User.objects.all().filter(type='buyer', is_staff=False)
    serializer_class = CompanySerializer