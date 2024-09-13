from django.urls import path
from . import views
from store.controller import authview, cart, wishlist, checkout, order

urlpatterns = [
    path('', views.index, name='index'),

    path('brands/', views.brands, name='brands'),
    path('brands/<str:slug>/', views.brand_view, name='brand_view'),
    path('brands/<str:brand_slug>/<str:prod_slug>/', views.product_view, name='product_view'),

    path('login/', authview.loginpage, name='loginpage'),
    path('register/', authview.register, name='register'),
    path('logout/', authview.logoutpage, name='logoutpage'),

    path("add-to-cart/", cart.addtocart, name='addtocart'),
    path("cart/", cart.cart, name='cart'),
    path("update-cart/", cart.updatecart, name="updatecart"),
    path("removecart/", cart.removecart, name="removecart"),

    path('wishlist/',wishlist.index, name='wishlist'),
    path('add-to-wishlist/', wishlist.addtowishlist, name='addtowishlist'),
    path('removewishlist/', wishlist.deleteitem, name='removewishlist'),

    path("checkout/", checkout.index, name="checkout"),
    path("placeorder/", checkout.placeorder, name="placeorder"),

    path('orders/', order.index, name='orders'),
    path('order/<str:t_no>/', order.orderview, name="orderview"),

    path("product-list/", views.productlist, name="productlist"),
    path("searchproduct/", views.searchproduct, name="searchproduct")
]
