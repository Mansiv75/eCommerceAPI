from django.urls import path
from .views import UserRegistrationView
from .views import CustomTokenObtainPairView
from .views import ProductListCreateView
from .views import ProductDetailView

urlpatterns=[
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('products/', ProductListCreateView.as_view(), name='products-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # <int:pk> is a placeholder for the primary key of the product.  # replace with the actual primary key field in your model.  # For example, 'id' if your model is named 'Product' and 'id' is the primary key.
]