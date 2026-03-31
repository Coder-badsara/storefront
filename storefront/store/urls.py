from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='ProductList'),
    path('products/<int:id>/', views.ProductDetail.as_view(), name='ProductDetail'),
    path('collections', views.collection_list, name='collection_list'),
    path('collections/<int:pk>', views.collection_detail, name='collection_detail'),
]
