from django.urls import path
from store import views
urlpatterns =[
    path('home/',views.home.as_view(),name="home"),
    path('register/',views.Register.as_view(),name="register"),
    path('list/',views.Collection.as_view(),name="li"),
    path('product/<int:pk>',views.Products.as_view(),name="pr"),
    path('product_detalis/<int:pk>',views.product_detail.as_view(),name="p_det"),
    path('log/',views.loginview.as_view(),name="login"),
    path("logout/",views.signout.as_view(),name="logout"),
    path('cart/<int:pk>',views.Addcart_view.as_view(),name="cart"),
    path('del/<int:pk>',views.Cartdelete.as_view(),name="delete"),
    path('cartall/',views.cartdetailview.as_view(),name="cartall"),
    path('order/<int:pk>',views.orderview.as_view(),name="order"),
    path('orderlist/',views.order_list.as_view(),name="orderlist"),
    path('delorder/<int:pk>',views.remove_order.as_view(),name="delorder"),
    path('search/',views.searchview.as_view(),name="search"),

]