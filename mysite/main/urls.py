# tells us the different views that we map to in views.py
# tells us view path, use decorators in flask?
from django.urls import path
from . import views # from current package import views module

urlpatterns = [
    path("<int:id>", views.index, name="index"), # home page, go to views.index, has name index, go to that page renders tech with tim header 1
    path("", views.home, name="home"),
    path("create/", views.create, name="create")
]