from django.contrib import admin
from .models import User, AuctionListing, Bid, Category, Comment, Watchlist


class BidAdmin(admin.ModelAdmin):
    list_display = ("get_listing_title", "bidder", "amount")

    def get_listing_title(self, obj):
        return obj.listing.title

    get_listing_title.short_description = "Listing Title"


class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("title", "start_bid", "creator", "created_at", "active")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("get_listing_title", "commenter", "created_on", "content")

    def get_listing_title(self, obj):
        return obj.listing.title

    get_listing_title.short_description = "Listing Title"


# Register your models here.
admin.site.register(Bid, BidAdmin)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
# admin.site.register(Watchlist)
# admin.site.register(User)
