from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
)

from .models import Company, Item, User, Address, Order, OrderItem, Review

class CompanySerializer(HyperlinkedModelSerializer):


    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field":"slug",
                "view_name":"Api-Company-Detail"
            }
        }
        

class ItemSerializer(HyperlinkedModelSerializer):

    company = CompanySerializer()

    class Meta:
        model = Item
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "Api-Item-Detail"
            }
        }


class UserSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "uid",
                "view_name": "Api-User-Detail"
            }
        }


class AddressSerializer(HyperlinkedModelSerializer):

    user = UserSerializer()
    
    class Meta:
        model = Address
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "Api-Address-Detail"
            }
        }


class OrderSerializer(HyperlinkedModelSerializer):

    user = UserSerializer()
    address = AddressSerializer()
        
    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "oid",
                "view_name": "Api-Order-Detail"
            }
        }


class OrderItemSerializer(HyperlinkedModelSerializer):

    order = OrderSerializer()
    item = ItemSerializer()
        
    class Meta:
        model = OrderItem
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "Api-OrderItem-Detail"
            }
        }

class ReviewSerializer(HyperlinkedModelSerializer):

    item = ItemSerializer()
    order = OrderSerializer()
        
    class Meta:
        model = Review
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "Api-Review-Detail"
            }
        }
