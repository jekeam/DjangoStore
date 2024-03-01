from django.urls import path

from .views import CanceledTemplateView, OrderCreateView, SuccessTemplateView

app_name = "orders"


urlpatterns = [
    path("order-create/", OrderCreateView.as_view(), name="order-create"),
    path("order-success/", SuccessTemplateView.as_view(), name="order-success"),
    path("order-canceled/", CanceledTemplateView.as_view(), name="order-canceled"),
]
