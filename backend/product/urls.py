from django.urls import path

from product.views import product_detail_view, product_create_view

urlpatterns = [
    path('', product_create_view),
    path('<int:pk>/', product_detail_view)  # pk - argument name is default one

]
