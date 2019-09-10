from backend import views
from django.urls import path

urlpatterns = [

    path('products/', views.AllProduct.as_view()),

    path('category/', views.Category.as_view()),
    path('products/filter/', views.Filter.as_view()),
    path('reviews', views.Reviews.as_view()),
    path('showcase', views.Showcase.as_view()),
    path('cartProducts/<int:pk>', views.CartProductsAPI.as_view())
   
]
