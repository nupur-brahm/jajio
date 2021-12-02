import uuid
from django.db.models.deletion import CASCADE
from django.urls import reverse
from improved_user.model_mixins import AbstractUser
from django.db import models
from django_extensions.db.fields import AutoSlugField

class User(AbstractUser):

    type = models.CharField(
        max_length=20,
        default="buyer"
    )
    verified = models.BooleanField(default=True)
    uid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    def __str__(self):
        return f"email: {self.email}, type: {self.type}"

    def get_absolute_url(self):
        return reverse(
            "auth:django_approve_company",
            kwargs={
                "pk": self.pk
            }
        )


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    short_name = models.CharField(max_length=20)
    slug = AutoSlugField(
        max_length=90,
        populate_from=["user__uid","short_name"]
    )
    line_1 = models.CharField(max_length=32)
    line_2 = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    pincode = models.IntegerField()
    country = models.CharField(max_length=32)