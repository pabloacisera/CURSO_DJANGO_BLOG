from django.urls import path
from .views import BlogViewList, BlogCreate, BlogUpdate, BlogDelete

app_name = "blog"

urlpatterns = [
    path("", BlogViewList.as_view(), name="home"),
    path("create/", BlogCreate.as_view(), name="create"),
    path("update/<int:pk>/", BlogUpdate.as_view(), name="update"),
    path('delete/<int:pk>/', BlogDelete.as_view(), name="delete"),
]
