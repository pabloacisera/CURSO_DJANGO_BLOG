from django.urls import path
from .views import BlogViewList
from.views import BlogCreate

app_name = "blog"

urlpatterns = [
    path("", BlogViewList.as_view(), name="home"),
    path("create/", BlogCreate.as_view(), name="create"),
]
