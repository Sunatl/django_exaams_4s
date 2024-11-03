from django.urls import path
from .views import *

urlpatterns = [
    path("",base,name="base"),
    
    # Movie
    path("Movie",MovieListView.as_view(),name="list_m"),
    path("detail_m/<int:pk>",MovieDetailView.as_view(),name="detail_m"),
    path("update_m/<int:pk>",MovieUpdateView.as_view(),name="update_m"),
    path("create_m",MovieCreateView.as_view(),name="create_m"),
    path("delete_m/<int:pk>",MovieDeleteView.as_view(),name="delete_m"),
    
    
    # Order
    path("Order",OrderListView.as_view(),name="list_o"),
    path("detail_o/<int:pk>",OrderDetailView.as_view(),name="detail_o"),
    path("update_o/<int:pk>",OrderUpdateView.as_view(),name="update_o"),
    path("create_o",OrderCreateView.as_view(),name="create_o"),
    path("delete_o/<int:pk>",OrderDeleteView.as_view(),name="delete_o"),
    
    # User
    path("User",UserListView.as_view(),name="list_u"),
    path("detail_u/<int:pk>",UserDetailView.as_view(),name="detail_u"),
    path("update_u/<int:pk>",UserUpdateView.as_view(),name="update_u"),
    path("create_u",UserCreateView.as_view(),name="create_u"),
    path("delete_u/<int:pk>",UserDeleteView.as_view(),name="delete_u"),
    
    
    # payment
    path("Payment",PaymentListView.as_view(),name="list_p"),
    path("detail_p/<int:pk>",PaymentDetailView.as_view(),name="detail_p"),
    path("update_p/<int:pk>",PaymentUpdateView.as_view(),name="update_p"),
    path("create_p",PaymentCreateView.as_view(),name="create_p"),
    path("delete_p/<int:pk>",PaymentDeleteView.as_view(),name="delete_p"),
    
    
    # Cinema
    path("Cinema",CinemaListView.as_view(),name="list_c"),
    path("detail_c/<int:pk>",CinemaDetailView.as_view(),name="detail_c"),
    path("update_c/<int:pk>",CinemaUpdateView.as_view(),name="update_c"),
    path("create_c",CinemaCreateView.as_view(),name="create_c"),
    path("delete_c/<int:pk>",CinemaDeleteView.as_view(),name="delete_c"),
    
    # genre
    path("Genre",GenreListView.as_view(),name="list_g"),
    path("detail_g/<int:pk>",GenreDetailView.as_view(),name="detail_g"),
    path("update_g/<int:pk>",GenreUpdateView.as_view(),name="update_g"),
    path("create_g",GenreCreateView.as_view(),name="create_g"),
    path("delete_g/<int:pk>",GenreDeleteView.as_view(),name="delete_g")
]
