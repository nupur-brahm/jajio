import uuid
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import CharField, IntegerField
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
from user.models import User, Address

DATETIME_FORMAT_STRING = "%A, %d %B %Y %I:%M%p"

# class Company(models.Model):
#     name = CharField(
#         max_length=48,
#         unique=True
#     )
#     slug = AutoSlugField(
#         max_length=20,
#         populate_from=["short_name"]
#     )
#     short_name = CharField(
#         max_length=20,
#         unique=True
#     )

#     class Meta:
#         ordering = ["name", "short_name"]

#     def __str__(self) -> str:
#         return f"{self.name} : {self.short_name}"

#     def get_absolute_url(self):
#         return reverse(
#             "company_detail",
#             kwargs={
#                 "slug" : self.slug
#             }
#         )


class Item(models.Model):
    name = models.CharField(
        max_length=63,
        db_index=True
    )
    slug = AutoSlugField(
        max_length=83,
        populate_from=["company__short_name","name"]
    )
    # images is an array of multiple image urls
    images = models.JSONField()
    """ 
    sizes = {
        {size} : {stock left}
        "M" : 20
    }
    """
    sizes = models.JSONField()
    # category
    company = models.ForeignKey(User, on_delete=CASCADE)
    # tags
    details = models.TextField(max_length=255)
    rating = models.FloatField()
    price = models.FloatField()
    discount = models.FloatField(default=0.0)
    
    class Meta:
        ordering = ["name"]
        unique_together = ("slug", "company")

    def __str__(self) -> str:
        return f"{self.company} : {self.name}"

    def get_absolute_url(self):
        return reverse(
            "item_detail", kwargs={"slug": self.slug}
        )
    
    def get_update_url(self):
        return reverse(
            "item_update", kwargs={"slug": self.slug}
        )
    
    def get_delete_url(self):
        return reverse(
            "item_delete", kwargs={"slug": self.slug}
        )
    
    def add_to_cart_url(self):
        return reverse(
            "move_item_to_cart", kwargs={"slug": self.slug}
        )


# class MyUser(models.Model):
#     uid = models.UUIDField(
#         default=uuid.uuid4,
#         unique=True,
#         editable=False
#     )
#     password = models.CharField(max_length=24)
#     name = models.CharField(max_length=48)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(unique=True, max_length=16)
#     gender = models.CharField(max_length=10)

#     class Meta:
#         ordering = ["name"]

#     def __str__(self) -> str:
#         return f"{self.name}: {self.email}"
    
#     def get_absolute_url(self):
#         return reverse(
#             "user_detail",
#             kwargs={
#                 "uid" : self.uid
#             }
#         )


# class Address(models.Model):
#     user = models.ForeignKey(MyUser,on_delete=CASCADE)
#     short_name = models.CharField(max_length=20)
#     slug = AutoSlugField(
#         max_length=90,
#         populate_from=["user__uid","short_name"]
#     )
#     line_1 = models.CharField(max_length=32)
#     line_2 = models.CharField(max_length=32)
#     city = models.CharField(max_length=32)
#     state = models.CharField(max_length=32)
#     pincode = models.IntegerField()
#     country = models.CharField(max_length=32)

#     class Meta:
#         ordering = ["user", "state", "city"]
#         unique_together = ("user", "line_1", "line_2", "city", "state", "pincode", "country")
#         unique_together = ("user", "short_name")
#     def __str__(self) -> str:
#         return f"{self.user}: , {self.line_1} {self.line_2} {self.city} {self.state} {self.pincode}"



class Order(models.Model):
    order_timestamp = models.DateTimeField()
    oid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    amount = models.FloatField()
    discount = models.FloatField(default=0.0)
    address = models.ForeignKey(Address, on_delete=DO_NOTHING)

    class Meta:
        get_latest_by = "order_timestamp"
        ordering = ["order_timestamp"]

    def __str__(self) -> str:
        date_time_string = self.order_timestamp.strftime(DATETIME_FORMAT_STRING)
        return f"{self.user}: {date_time_string}"



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    item = models.ForeignKey(Item, on_delete=CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10)


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=DO_NOTHING)
    slug = AutoSlugField(
        max_length=83,
        populate_from=["order__oid","item__id"]
    )
    order = models.ForeignKey(Order, on_delete=CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    discount = models.FloatField(default=0.0)
    delivery_timestamp = models.DateTimeField()
    payment_timestamp = models.DateTimeField()
    payment_type = models.CharField(max_length=20)

    class Meta:
        get_latest_by = "delivery_timestamp"
        ordering = ["order", "item"]


    def __str__(self) -> str:
        return f"{self.order}: {self.item}"


class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=CASCADE)
    slug = AutoSlugField(
        max_length=83,
        populate_from=["order__oid","item__id"]
    )
    order = models.ForeignKey(Order, on_delete=CASCADE)
    timestamp = models.DateTimeField()
    images = models.JSONField()
    rating = IntegerField()
    description = models.TextField()

    class Meta:
        get_latest_by = "timestamp"
        ordering = ["item", "rating"]

    def __str__(self) -> str:
        return f"{self.order_id}: {self.item_id}"
