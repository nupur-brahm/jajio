from django.urls import path

from .views import(
    CompanyDetail,
    CompanyList,
    CompanyCreate,
    CompanyDelete,
    CompanyUpdate,
)

urlpatterns = [
    path("company/", CompanyList.as_view(), name="company_list"),
    path(
        "company/create/",
        CompanyCreate.as_view(),
        name="company_create"
    ),
    path(
        "company/<str:slug>/",
        CompanyDetail.as_view(),
        name="company_detail"
    ),
    path(
        "company/<str:slug>/update/",
        CompanyUpdate.as_view(),
        name="company_update"
    ),
    path(
        "company/<str:slug>/delete/",
        CompanyDelete.as_view(),
        name="company_delete"
    ),
]