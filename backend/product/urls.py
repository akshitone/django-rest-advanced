from django.urls import path

from product.views import product_detail_view

urlpatterns = [
    path('<int:product_id>/', product_detail_view.as_view())
]
