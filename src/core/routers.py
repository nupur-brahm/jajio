from django.urls import path

from .views import (
    CompanyApiDetail, 
    CompanyApiList,
    ItemApiDetail,
    ItemApiList,
    UserApiDetail,
    UserApiList,
    AddressApiDetail,
    AddressApiList,
    OrderApiDetail,
    OrderApiList,
    OrderItemApiDetail,
    OrderItemApiList,
    ReviewApiDetail,
    ReviewApiList,
)


urlpatterns = [
    path("company/", CompanyApiList.as_view(), name="Api-Company-List"),
    path("company/<str:slug>/", CompanyApiDetail.as_view(), name="Api-Company-Detail"),
    path("item/", ItemApiList.as_view(), name="Api-Item-List"),
    path("item/<str:slug>/", ItemApiDetail.as_view(), name="Api-Item-Detail"),
    path("user/", UserApiList.as_view(), name="Api-User-List"),
    path("user/<str:uid>/", UserApiDetail.as_view(), name="Api-User-Detail"),
    path("address/", AddressApiList.as_view(), name="Api-Address-List"),
    path("address/<str:slug>/", AddressApiDetail.as_view(), name="Api-Address-Detail"),
    path("order/", OrderApiList.as_view(), name="Api-Order-List"),
    path("order/<str:oid>/", OrderApiDetail.as_view(), name="Api-Order-Detail"),
    path("orderitem/", OrderItemApiList.as_view(), name="Api-OrderItem-List"),
    path("orderitem/<str:slug>/", OrderItemApiDetail.as_view(), name="Api-OrderItem-Detail"),
    path("review/", ReviewApiList.as_view(), name="Api-Review-List"),
    path("review/<str:slug>/", ReviewApiDetail.as_view(), name="Api-Review-Detail"),
]