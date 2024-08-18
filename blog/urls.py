from django.urls import path
from .views import BlogViewList

app_name = "blog"

urlpatterns = [
    path("", BlogViewList.as_view(), name="home"),
]
