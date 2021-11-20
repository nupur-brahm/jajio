from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
)

from .models import Company, Item, MyUser, Address, Order, OrderItem, Review

class CompanySerializer(HyperlinkedModelSerializer):


    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field":"slug",
                "view_name":"api-company-detail"
            }
        }
        

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


class MyUserSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = MyUser
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "uid",
                "view_name": "api-user-detail"
            }
        }


class AddressSerializer(HyperlinkedModelSerializer):

    user = MyUserSerializer(read_only=True)
    
    class Meta:
        model = Address
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-address-detail"
            }
        }


class OrderSerializer(HyperlinkedModelSerializer):

    user = MyUserSerializer(read_only=True)
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
