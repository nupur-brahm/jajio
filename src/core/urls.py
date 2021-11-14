from django.urls import path

from .views import(
    UserDetail,
    UserList,
    UserCreate,
    UserDelete,
    UserUpdate,
)

urlpatterns = [
    path("user/", UserList.as_view(), name="user_list"),
    path(
        "user/create/",
        UserCreate.as_view(),
        name="user_create"
    ),
    path(
        "user/<str:uid>/",
        UserDetail.as_view(),
        name="user_detail"
    ),
    path(
        "user/<str:uid>/update/",
        UserUpdate.as_view(),
        name="user_update"
    ),
    path(
        "user/<str:uid>/delete/",
        UserDelete.as_view(),
        name="user_delete"
    ),
]