from django.contrib import admin
from .models import User, AuctionListing, Bid, Category, Comment, Watchlist

# Register your models here.
admin.site.register(Bid)
admin.site.register(AuctionListing)
admin.site.register(Comment)
admin.site.register(Category)

# admin.site.register(Watchlist)
# admin.site.register(User)
