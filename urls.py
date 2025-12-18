"""
URL configuration for shopkart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product import views as productView
from account import views as accountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',accountView.signup,name='signup'),
    path('signin/',accountView.signin,name='signin'),
    path('signout/',accountView.signout,name='signout'),
    path('forgot-password/',accountView.forgotPassword,name='forgot_password'),
    path('verify-otp/',accountView.verifyOtp,name='verify_otp'),
    path('reset-password/<int:user_id>/',accountView.resetPassword,name="reset_password"),
    
    
    
    path('',productView.index,name='index'),
    path('product-details/<int:pk>/',productView.productDetails,name="product_details"),
    path("add-to-cart/<int:pk>/",productView.addToCart,name='addToCart'),
    path("buy-now/<int:pk>/",productView.buyNow,name='buy_now'),
    path('cart/',productView.cart,name='cart'),
    path('updateqty/<int:pk>/',productView.updateQty,name='updateqty'),
    path('remove-item/<int:pk>/',productView.removeItem,name='remove_item'),
    path('address/',productView.address,name='address'),
    path('update-address/<int:id>/',productView.updateAddress,name='update_address'),
    path('remove-address/<int:id>/',productView.removeAddress,name='remove_address'),
    path('confirm-order/<int:id>/',productView.confirmOrder,name='confirm_order'),
    path('pay/<int:id>/',productView.pay,name='pay'),
    path('payment-success/',productView.paymentSuccess,name='payment_success')
    
    
    
]

from django.conf import settings
from django.conf.urls.static import  static


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
