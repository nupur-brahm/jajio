from django.shortcuts import (
    get_list_or_404,
    get_object_or_404
)
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from .serializers import CompanySerializer, ItemSerializer, UserSerializer, AddressSerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer
from .models import Company, Item, User, Address, Order, OrderItem, Review

class CompanyApiDetail(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = "slug"

class CompanyApiList(ListAPIView):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ItemApiDetail(RetrieveAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "slug"

class ItemApiList(ListAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UserApiDetail(RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "uid"

class UserApiList(ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddressApiDetail(RetrieveAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = "slug"

class AddressApiList(ListAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class OrderApiDetail(RetrieveAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "pk"

class OrderApiList(ListAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemApiDetail(RetrieveAPIView):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = "slug"

class OrderItemApiList(ListAPIView):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class ReviewApiDetail(RetrieveAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "slug"

class ReviewApiList(ListAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
