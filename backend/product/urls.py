from django.urls import path

from product.views import product_detail_view

urlpatterns = [
    path('<int:pk>/', product_detail_view)  # pk - argument name is default one
]
