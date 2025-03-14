from django.urls import path
from .views import *
app_name = 'products'

urlpatterns = [
    path('', IndexView, name='index'),
    path('farmer-dash/', FarmerDashView, name='farmer_dash'),
    path('about/', AboutView, name='about'),
    path('products/',  ProductView, name='products'),
    path('products-list/',  ProductListView, name='products-list'),
    path('add-crop/', AddProductView, name='add-crop'),
    path('edit-crop/<int:id>/', EditProductView, name='edit-crop'),
    path('<int:id>/<slug:slug>/',  ProductDetailView, name='products-detail'),
    path('<slug:category_slug>/',  ProductListView, name='products-list-by-category'),
    # path('crop-details/<int:id>/', FarmerProductView, name='product-details'),
]
