from django.urls import path,include
from .views import temp_humi_detail, temp_humi_list

urlpatterns = [
    path("",temp_humi_list),
    path("<int:id>",temp_humi_detail),
]