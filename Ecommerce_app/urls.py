
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category_items/<int:category_id>/',views.category_items, name="category_items"),
    path('quick_view/<int:quick_view_id>/', views.quick_view, name="quick_view"),
    path('search_products/', views.search_products, name="search_products"),
    path('all_products/', views.all_products, name="all_products"),
    path("my_products/", views.my_products, name="my_products"),
    path("add_product/", views.add_product, name="add_product"),
    path("update_product/<int:id>", views.update_product, name="update_product"),
    path("delete_product/<int:id>/", views.delete_product, name="delete_product"),
    path("feedBack/<int:quick_view_id>/", views.feedBack, name="feedBack"),
    path("DeleteFeedback/<int:id>/", views.DeleteFeedback, name="DeleteFeedback"),
    path("UpdateFeedback/<int:id>/", views.UpdateFeedback, name="UpdateFeedback"),

    path("Order/<int:quick_view_id>/", views.Order, name="Order"),
    path("OrderList/", views.OrderList, name="OrderList"),
    path("OrderTracking/", views.OrderTracking, name="OrderTracking"),
    path('DeleteOrder/<int:id>', views.DeleteOrder, name="DeleteOrder"),

    
    path('ShoppinfCart/<int:id>', views.ShoppinfCart, name="ShoppinfCart"),
    path('DeleteCartItem/<int:id>', views.DeleteCartItem, name="DeleteCartItem"),   
    
  
]