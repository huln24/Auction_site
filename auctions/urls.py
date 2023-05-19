from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("categories", views.categories, name="categories"),
    path("listing/<str:id>/<str:title>", views.listing, name="listing"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),
    path("listing/<str:id>/<str:title>/bid_error", views.bid_error, name="bid_error"),
    path("my_listings", views.my_listings, name="my_listings"),
    path("my_bids", views.my_bids, name="my_bids"),
]
