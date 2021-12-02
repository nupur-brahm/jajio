from django.contrib import admin


from .models import Cart, Item, Order, OrderItem, Review
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(MyUser)
# admin.site.register(Address)
admin.site.register(Review)
admin.site.register(Cart)

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
