from django.urls import path
from django.urls.base import reverse_lazy

from .views import(
    # CompanyDetail,
    # CompanyList,
    # CompanyCreate,
    # CompanyDelete,
    # CompanyUpdate,
    ItemDetail,
    ItemList,
    ItemCreate,
    ItemDelete,
    ItemUpdate,
    MoveItemToCart,
    CartDetail,
)

urlpatterns = [
    # path("company/", CompanyList.as_view(), name="company_list"),
    # path(
    #     "company/create/",
    #     CompanyCreate.as_view(),
    #     name="company_create"
    # ),
    # path(
    #     "company/<str:slug>/",
    #     CompanyDetail.as_view(),
    #     name="company_detail"
    # ),
    # path(
    #     "company/<str:slug>/update/",
    #     CompanyUpdate.as_view(),
    #     name="company_update"
    # ),
    # path(
    #     "company/<str:slug>/delete/",
    #     CompanyDelete.as_view(),
    #     name="company_delete"
    # ),
    path("item/", ItemList.as_view(), name="item_list"),
    path(
        "item/create/",
        ItemCreate.as_view(),
        name="item_create"
    ),
    path(
        "item/<str:slug>/",
        ItemDetail.as_view(),
        name="item_detail"
    ),
    path(
        "item/<str:slug>/update/",
        ItemUpdate.as_view(),
        name="item_update"
    ),
    path(
        "item/<str:slug>/delete/",
        ItemDelete.as_view(),
        name="item_delete"
    ),
    path("cart/", CartDetail.as_view(), name="cart"),
    path(
        "item/<str:slug>/move_to_cart/",
        MoveItemToCart.as_view(success_url=reverse_lazy("cart")),
        name="move_item_to_cart"
    ),
]