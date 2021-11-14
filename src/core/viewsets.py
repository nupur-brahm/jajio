from rest_framework.viewsets import ModelViewSet

from .models import(
    User,
    Company,
    Item,
    Address,
    Order,
    OrderItem,
    Review,
)
from .serializers import(
    UserSerializer,
    CompanySerializer,
    ItemSerializer,
    AddressSerializer,
    OrderSerializer,
    OrderItemSerializer,
    ReviewSerializer,
)


class CompanyViewSet(ModelViewSet):

    lookup_field = "slug"
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ItemViewSet(ModelViewSet):

    lookup_field = "slug"
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UserViewSet(ModelViewSet):

    lookup_field = "uid"
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressViewSet(ModelViewSet):

    lookup_field = "slug"
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class OrderViewSet(ModelViewSet):

    lookup_field = "oid"
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):

    lookup_field = "slug"
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class ReviewViewSet(ModelViewSet):

    lookup_field = "slug"
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer