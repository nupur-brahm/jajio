from django.urls import path
from .views import (
    CompanyApiDetail, 
    CompanyApiList,
    BuyerApiDetail,
    BuyerApiList,
)


urlpatterns =[
    path("company/", CompanyApiList.as_view(), name="Api-Company-List"),
    path("company/<str:uid>/", CompanyApiDetail.as_view(), name="Api-Company-Detail"),
    path("buyer/", BuyerApiList.as_view(), name="Api-Buyer-List"),
    path("buyer/<str:uid>/", BuyerApiDetail.as_view(), name="Api-Buyer-Detail"),
]