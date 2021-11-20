from django.contrib import admin


from .models import Company, Item, Order, OrderItem, MyUser, Address, Review
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(MyUser)
admin.site.register(Address)
admin.site.register(Review)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = ("name", "slug", "short_name")

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "images",
        "sizes",
        "company",
        "details",
        "rating",
        "price",
        "discount"
    )
