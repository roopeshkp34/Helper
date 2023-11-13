from django.urls import path
from master.views import main

urlpatterns = [
    path("", main.index, name="Home"),
    path("save", main.save, name="save"),
    path("search_user", main.search_user, name="search_user")

]