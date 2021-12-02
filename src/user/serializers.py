from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User, Address


class CompanySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["full_name", "short_name"]
        extra_kwargs = {
            "url": {
                "lookup_field": "uid",
                "view_name": "Api-Company-Detail"
            }
        }


class BuyerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["full_name", "short_name"]
        extra_kwargs = {
            "url": {
                "lookup_field": "uid",
                "view_name": "Api-User-Detail"
            }
        }


class AddressSerializer(HyperlinkedModelSerializer):

    user = BuyerSerializer(read_only=True)
    
    class Meta:
        model = Address
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-address-detail"
            }
        }