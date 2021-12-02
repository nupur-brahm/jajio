from django.db.models import Q
from django.core.exceptions import ImproperlyConfigured


def get_perms(string_perm):
    """Build Q() of permission identified by string_perm

    expects: contenttypes.add_contenttype or contenttypes.*
    """
    if "." not in string_perm:
        raise ImproperlyConfigured(
            "The permission in the perms argument needs to be either "
            "app_label.codename or app_label.* "
            "(e.g. contenttypes.add_contenttype or contenttypes.*)"
        )
    app_label, codename = string_perm.split(".")
    if codename == "*":
        return Q(content_type__app_label=app_label)
    else:
        return Q(
            content_type__app_label=app_label,
            codename=codename,
        )
