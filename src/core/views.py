
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
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
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from .forms import ItemForm, ItemToCartForm

from .serializers import CompanySerializer, ItemSerializer, AddressSerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer
from .models import Cart, Item, Order, OrderItem, Review
# from user.models import User as Company

# class CompanyApiDetail(RetrieveAPIView):
#     queryset = Company.objects.all().filter(type='company')
#     serializer_class = CompanySerializer
#     lookup_field = "uid"

# class CompanyApiList(ListAPIView):

#     queryset = Company.objects.all().filter(type='company')
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

# class CompanyList(ListView):

#     queryset = Company.objects.all()
#     template_name = "company/list.html"

# class CompanyDetail(DetailView):
    
#     queryset = Company.objects.all()
#     template_name = "company/detail.html"
#     # slug_field = "uid"
#     # slug_url_kwarg = "uid"

# class CompanyCreate(PermissionRequiredMixin, CreateView):
#     form_class = CompanyForm
#     model = Company
#     permission_required = "company.add_company"
#     template_name = "company/form.html"
#     extra_context = {"update": False}

# class CompanyUpdate(PermissionRequiredMixin, UpdateView):
#     form_class = CompanyForm
#     model = Company
#     permission_required = "company.change_company"
#     template_name = "company/form.html"
#     extra_context = {"update": True}
#     # slug_field = "uid"
#     # slug_url_kwarg = "uid"

# class CompanyDelete(PermissionRequiredMixin, DeleteView):
#     model = Company
#     permission_required = "company.delete_company"
#     template_name = "company/confirm_delete.html"
#     success_url = reverse_lazy("company_list")


class ItemList(PermissionRequiredMixin, ListView):

    queryset = Item.objects.all()
    permission_required = "core.view_item"
    template_name = "item/list.html"

    def get(self, request, *args, **kwargs):
        company = request.user
        self.object_list = self.get_queryset().filter(company=company)
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)

class ItemDetail(PermissionRequiredMixin, DetailView):
    
    queryset = Item.objects.all()
    permission_required = "core.view_item"
    template_name = "item/detail.html"

class ItemCreate(PermissionRequiredMixin, CreateView):

    form_class = ItemForm
    model = Item
    permission_required = "core.add_item"
    template_name = "item/form.html"
    extra_context = {"update": False}


    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
            form.instance.company = user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ItemUpdate(PermissionRequiredMixin, UpdateView):
    form_class = ItemForm
    model = Item
    permission_required = "core.change_item"
    template_name = "item/form.html"
    extra_context = {"update": True}

class ItemDelete(PermissionRequiredMixin, DeleteView):
    model = Item
    permission_required = "core.delete_item"
    template_name = "item/confirm_delete.html"
    success_url = reverse_lazy("item_list")


class CartDetail(LoginRequiredMixin, ListView):
    queryset = Cart.objects.all()
    template_name = "cart/detail.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        self.object_list = self.get_queryset().filter(user=user)
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)


class ListAllItems(ListView):
    queryset = Item.objects.all()
    template_name = "root.html"


class MoveItemToCart(CreateView):
    form_class = ItemToCartForm
    model = Cart
    template_name = "cart/add_item_form.html"
    extra_context = {"update": False}

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
            form.instance.user = user
            item_slug = kwargs["slug"]
            form.instance.item = Item.objects.get(slug=item_slug)
            print(form.instance.user.short_name)
            print(item_slug)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
