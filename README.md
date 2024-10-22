
---

# 🛒 Django E-Commerce API

This is a fully functional e-commerce backend API built with Django and Django Rest Framework (DRF). It supports user authentication, product management, shopping cart operations, and checkout with payment gateway integration. The API documentation is available via both Swagger and Redoc.

## 🚀 Features

- **User Authentication** (Register, Login, Logout)
- **Product Management** (Add to Cart, Remove from Cart, Search Products)
- **Shopping Cart** (View products, Add, and Remove items)
- **Checkout and Payment** (Checkout with integrated payment gateways)
- **API Documentation** (Swagger and Redoc)

## 🛠️ Tech Stack

- **Framework**: Django, Django Rest Framework (DRF)
- **Authentication**: JWT (JSON Web Token) with SimpleJWT
- **Database**: SQLite (easily swappable with PostgreSQL, MySQL, etc.)
- **Documentation**: Swagger, Redoc

## 📄 API Documentation

### Local Development Documentation
- **Swagger UI**: [Swagger Documentation](http://127.0.0.1:8000/api/swagger/)
- **Redoc UI**: [Redoc Documentation](http://127.0.0.1:8000/api/redoc/)

### Live API Documentation (https://ecommerceapi-1-m2vv.onrender.com)
- **Swagger UI**: [Swagger Documentation](https://ecommerceapi-1-m2vv.onrender.com/api/swagger/)
- **Redoc UI**: [Redoc Documentation](https://ecommerceapi-1-m2vv.onrender.com/api/redoc/)

## 📂 Project Structure


```bash
eCommerceAPI/
├── eCommerceAPI/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── core/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── static/
│   └── (static files for the project)
├── db.sqlite3 (or the name of your database file)
├── manage.py
├── requirements.txt
├── .env
```


## 📝 API Endpoints

### User Endpoints
- **POST /api/auth/signup/**: Register a new user
- **POST /api/auth/login/**: Log in a user
- **POST /api/auth/logout/**: Log out a user

### Product Endpoints
- **GET /api/products/**: List all products
- **GET /api/products/{id}/**: Get details of a specific product
- **GET /api/products/search?=keyword**: Search products by keyword

### Cart Endpoints
- **POST /api/cart/add/**: Add a product to the cart
- **POST /api/cart/remove/**: Remove a product from the cart
- **GET /api/cart/**: View all items in the cart

### Checkout and Payment Endpoints
- **POST /api/checkout/**: Checkout and initiate payment

## 🛠️ Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mansiv75/eCommerceAPI.git
   cd ecommerce-api
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the API**:
   - **Base URL**: `https://ecommerceapi-1-m2vv.onrender.com`
   
## 📬 Contact

For any questions or feedback, feel free to reach out to me at [mv072004@gmail.com](mailto:mv072004@gmail.com).

---
https://roadmap.sh/projects/ecommerce-api
