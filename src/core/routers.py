from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import (
#     CompanyApiDetail, 
#     CompanyApiList,
#     ItemApiDetail,
#     ItemApiList,
#     MyUserApiDetail,
#     MyUserApiList,
#     AddressApiDetail,
#     AddressApiList,
#     OrderApiDetail,
#     OrderApiList,
#     OrderItemApiDetail,
#     OrderItemApiList,
#     ReviewApiDetail,
#     ReviewApiList,
# )
from .viewsets import(
    CompanyViewSet,
    ItemViewSet,
    MyUserViewSet,
    AddressViewSet,
    OrderViewSet,
    OrderItemViewSet,
    ReviewViewSet,
)

api_router = DefaultRouter()
api_router.register("company", CompanyViewSet, basename="api-company")
api_router.register("item", ItemViewSet, basename="api-item")
api_router.register("user", MyUserViewSet, basename="api-user")
api_router.register("address", AddressViewSet, basename="api-address")
api_router.register("order", OrderViewSet, basename="api-order")
api_router.register("orderitem", OrderItemViewSet, basename="api-orderitem")
api_router.register("review", ReviewViewSet, basename="api-review")
api_routes = api_router.urls

urlpatterns = api_routes + [
    # path("company/", CompanyApiList.as_view(), name="Api-Company-List"),
    # path("company/<str:slug>/", CompanyApiDetail.as_view(), name="Api-Company-Detail"),
    # path("item/", ItemApiList.as_view(), name="Api-Item-List"),
    # path("item/<str:slug>/", ItemApiDetail.as_view(), name="Api-Item-Detail"),
    # path("user/", MyUserApiList.as_view(), name="Api-MyUser-List"),
    # path("user/<str:uid>/", MyUserApiDetail.as_view(), name="Api-MyUser-Detail"),
    # path("address/", AddressApiList.as_view(), name="Api-Address-List"),
    # path("address/<str:slug>/", AddressApiDetail.as_view(), name="Api-Address-Detail"),
    # path("order/", OrderApiList.as_view(), name="Api-Order-List"),
    # path("order/<str:oid>/", OrderApiDetail.as_view(), name="Api-Order-Detail"),
    # path("orderitem/", OrderItemApiList.as_view(), name="Api-OrderItem-List"),
    # path("orderitem/<str:slug>/", OrderItemApiDetail.as_view(), name="Api-OrderItem-Detail"),
    # path("review/", ReviewApiList.as_view(), name="Api-Review-List"),
    # path("review/<str:slug>/", ReviewApiDetail.as_view(), name="Api-Review-Detail"),
]