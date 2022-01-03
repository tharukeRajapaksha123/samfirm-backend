from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeView,name="home"),
    path('add-link',views.addFileLink,name="add_file_link"),
    path('add-post',views.addFileLink,name="add_post"),
    path('get-links',views.getFirmwareLins,name="get_firmware_link")
]