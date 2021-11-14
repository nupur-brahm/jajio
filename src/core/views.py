from django import template
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import(
    DetailView,
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .forms import UserForm

from .serializers import CompanySerializer, ItemSerializer, UserSerializer, AddressSerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer
from .models import Company, Item, User, Address, Order, OrderItem, Review

# class CompanyApiDetail(RetrieveAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     lookup_field = "slug"

# class CompanyApiList(ListAPIView):

#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

# class ItemApiDetail(RetrieveAPIView):

#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     lookup_field = "slug"

# class ItemApiList(ListAPIView):

#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class UserApiDetail(RetrieveUpdateDestroyAPIView):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = "uid"

# class UserApiList(ListCreateAPIView):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class AddressApiDetail(RetrieveAPIView):

#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
#     lookup_field = "slug"

# class AddressApiList(ListAPIView):

#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer

# class OrderApiDetail(RetrieveAPIView):

#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     lookup_field = "pk"

# class OrderApiList(ListAPIView):

#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class OrderItemApiDetail(RetrieveAPIView):

#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#     lookup_field = "slug"

# class OrderItemApiList(ListAPIView):

#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer

# class ReviewApiDetail(RetrieveAPIView):

#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     lookup_field = "slug"

# class ReviewApiList(ListAPIView):

#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

class UserList(ListView):

    queryset = User.objects.all()
    template_name = "user/list.html"

class UserDetail(DetailView):
    
    queryset = User.objects.all()
    template_name = "user/detail.html"
    slug_field = "uid"
    slug_url_kwarg = "uid"

class UserCreate(CreateView):
    form_class = UserForm
    model = User
    template_name = "user/form.html"
    extra_context = {"update": False}

class UserUpdate(UpdateView):
    form_class = UserForm
    model = User
    template_name = "user/form.html"
    extra_context = {"update": True}
    slug_field = "uid"
    slug_url_kwarg = "uid"

class UserDelete(DeleteView):
    model = User
    template_name = "user/confirm_delete.html"
    success_url = reverse_lazy("user_list.html")



