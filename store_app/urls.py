from django.contrib import admin
from django.urls import path 

from .views import (
    StoreListView,
    StoreCreateView,
    StoreUpdateView, 
    StoreDeleteView,

)

app_name = "store"

urlpatterns = [
    path("", StoreListView.as_view(), name="all"),
    path("create/", StoreCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", StoreDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", StoreUpdateView.as_view(), name="update")
]