from rest_framework.viewsets import ModelViewSet

from .models import(
    Item,
    Order,
    OrderItem,
    Review,
)
from .serializers import(
    ItemSerializer,
    OrderSerializer,
    OrderItemSerializer,
    ReviewSerializer,
)


class ItemViewSet(ModelViewSet):

    lookup_field = "slug"
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



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