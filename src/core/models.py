from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import IntegerChoices
from django.db.models.fields import CharField, PositiveIntegerField
from django_postgres_extensions.models.fields import ArrayField, JSONField

DATETIME_FORMAT_STRING = "%A, %d %B %Y %I:%M%p"
class Company(models.Model):
    name = CharField(
        max_length=48,
        unique=True
    )
    slug = models.SlugField(max_length=48)
    short_name = CharField(
        max_length=20,
        unique=True
    )

    class Meta:
        ordering = ["name", "short_name"]

    def __str__(self) -> str:
        return f"{self.name} : {self.short_name}"


class Item(models.Model):
    name = models.CharField(
        max_length=63,
        db_index=True
    )
    slug = models.SlugField(max_length=63)
    # images is an array of multiple image urls
    images = ArrayField()
    link = models.URLField()
    """ 
    sizes = {
        {size} : {stock left}
        "M" : 20
    }
    """
    sizes = models.JSONField()
    # category
    company = models.ForeignKey(Company, on_delete=CASCADE)
    # tags
    details = models.TextField(max_length=255)
    rating = models.IntegerChoices()
    price = models.FloatField()
    discount = models.FloatField(default=0.0)
    
    class Meta:
        ordering = ["name"]
        unique_together = ("slug", "company")

    def __str__(self) -> str:
        return f"{self.company} : {self.name}"


class User(models.Model):
    password = models.CharField()
    name = models.CharField()
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True)
    gender = models.TextChoices()

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name}: {self.email}"


class Address(models.Model):
    user = models.ForeignKey(User)
    line_1 = models.CharField(max_length=32)
    line_2 = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.TextChoices()
    pincode = models.IntegerField()
    country = models.TextChoices()

    class Meta:
        ordering = ["user", "state", "city"]
        unique_together = ("user", "line_1", "line_2", "city", "state", "pincode", "country")

    def __str__(self) -> str:
        return f"{self.user}: , {self.line_1} {self.line_2} {self.city} {self.state} {self.pincode}"


class Order(models.Model):
    order_timestamp = models.DateTimeField()
    user = models.ForeignKey(User)
    amount = models.FloatField()
    discount = models.FloatField(default=0.0)
    address = models.ForeignKey(Address)

    class Meta:
        get_latest_by = "order_timestamp"
        ordering = ["order_timestamp"]

    def __str__(self) -> str:
        date_time_string = self.order_timestamp.strftime(DATETIME_FORMAT_STRING)
        return f"{self.user}: {date_time_string}"


class OrderItem(models.Model):
    item = models.ForeignKey(Item)
    order = models.ForeignKey(Order)
    quantity = models.PositiveIntegerField(default=1)
    discount = models.FloatField(default=0.0)
    delivery_timestamp = models.DateTimeField()
    payment_timestamp = models.DateTimeField()
    payment_type = models.TextChoices()

    class Meta:
        get_latest_by = "delivery_timestamp"
        ordering = ["order", "item"]


    def __str__(self) -> str:
        return f"{self.order}: {self.item}"


class Review(models.Model):
    item_id = models.ForeignKey(Item, on_delete=CASCADE)
    order_id = models.ForeignKey(Order, on_delete=CASCADE)
    timestamp = models.DateTimeField()
    images = ArrayField()
    rating = IntegerChoices()
    description = models.TextField()

    class Meta:
        get_latest_by = "timestamp"
        ordering = ["item", "rating"]

    def __str__(self) -> str:
        return f"{self.order_id}: {self.item_id}"
