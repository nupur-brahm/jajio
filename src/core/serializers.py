from rest_framework.serializers import (
    HyperlinkedModelSerializer
)
from user.serializers import(
    CompanySerializer,
    BuyerSerializer,
    AddressSerializer,
)
from .models import Item, Order, OrderItem, Review


class ItemSerializer(HyperlinkedModelSerializer):

    company = CompanySerializer(read_only=True)

    class Meta:
        model = Item
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-item-detail"
            }
        }


class OrderSerializer(HyperlinkedModelSerializer):

    user = BuyerSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
        
    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "oid",
                "view_name": "api-order-detail"
            }
        }


class OrderItemSerializer(HyperlinkedModelSerializer):

    order = OrderSerializer(read_only=True)
    item = ItemSerializer(read_only=True)
        
    class Meta:
        model = OrderItem
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-orderitem-detail"
            }
        }


class ReviewSerializer(HyperlinkedModelSerializer):

    item = ItemSerializer(read_only=True)
    order = OrderSerializer(read_only=True)
        
    class Meta:
        model = Review
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-review-detail"
            }
        }
