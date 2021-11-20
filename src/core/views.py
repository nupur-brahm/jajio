from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
)
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

from .forms import CompanyForm

from .serializers import CompanySerializer, ItemSerializer, MyUserSerializer, AddressSerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer
from .models import Company, Item, MyUser, Address, Order, OrderItem, Review

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

# class MyUserApiDetail(RetrieveUpdateDestroyAPIView):

#     queryset = MyUser.objects.all()
#     serializer_class = MyUserSerializer
#     lookup_field = "uid"

# class MyUserApiList(ListCreateAPIView):

#     queryset = MyUser.objects.all()
#     serializer_class = MyUserSerializer

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

class CompanyList(ListView):

    queryset = Company.objects.all()
    template_name = "company/list.html"

class CompanyDetail(DetailView):
    
    queryset = Company.objects.all()
    template_name = "company/detail.html"
    # slug_field = "uid"
    # slug_url_kwarg = "uid"

class CompanyCreate(PermissionRequiredMixin, CreateView):
    form_class = CompanyForm
    model = Company
    permission_required = "company.add_company"
    template_name = "company/form.html"
    extra_context = {"update": False}

class CompanyUpdate(PermissionRequiredMixin, UpdateView):
    form_class = CompanyForm
    model = Company
    permission_required = "company.change_company"
    template_name = "company/form.html"
    extra_context = {"update": True}
    # slug_field = "uid"
    # slug_url_kwarg = "uid"

class CompanyDelete(PermissionRequiredMixin, DeleteView):
    model = Company
    permission_required = "company.delete_company"
    template_name = "company/confirm_delete.html"
    success_url = reverse_lazy("company_list")



