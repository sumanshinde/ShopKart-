# ShopKart Project Guide

## Overview
ShopKart is an e-commerce web application built with **Django**. It features user authentication, product browsing, cart management, and order processing with **Razorpay** integration.

## Project Structure
The project is organized into apps:

### 1. `account` App
Handles user management and authentication.
- **Models**:
    - `User`: Custom user model using email as the username.
    - `Shipping_Address`: Stores user shipping details.
- **Features**: Signup, Signin, Password Reset (OTP based).

### 2. `product` App
Handles the core e-commerce functionality.
- **Models**:
    - `Category` & `Product`: Manages product catalog.
    - `Cart`: Manages user's shopping cart.
    - `Order` & `OrderItem`: Handles order processing.
- **Features**:
    - Product listing and details.
    - Cart operations (Add, Remove, Update Quantity).
    - Checkout flow (Address selection, Payment).
    - Razorpay payment integration.

### Key Files
- `shopkart/settings.py`: Project configuration (Apps, Database, Static files).
- `shopkart/urls.py`: Main routing configuration.
- `manage.py`: Django's command-line utility.

## How to Run the Project

### Prerequisites
- Python installed.
- Virtual environment (recommended).

### Steps
1.  **Set up Environment & Install Dependencies**:
    > **For Learners**: Take this project for reference and create your own environment.
    
    Install the required modules:
    ```bash
    pip install django pillow razorpay
    ```
    OR (using the requirements file):
    ```bash
    pip install -r requirements.txt
    ```

2.  **Apply Migrations** (Set up the database):
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3.  **Run Development Server**:
    ```bash
    python manage.py runserver
    ```

4.  **Access the App**:
    Open [http://localhost:8000](http://localhost:8000) in your browser.

## Admin Panel
Create a superuser to access the Django Admin interface:
```bash
python manage.py createsuperuser
```
Access at [http://localhost:8000/admin](http://localhost:8000/admin).
