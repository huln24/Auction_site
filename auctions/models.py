from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f"{self.name}"


class AuctionListing(models.Model):
    title = models.CharField(max_length=64, blank=False)  # Field is required
    description = models.TextField(
        blank=True
    )  # Field not required, if empty, empty string('') will be saved in db
    start_bid = models.DecimalField(
        max_digits=1000, decimal_places=2, blank=False
    )  # Field is required
    image = models.URLField(blank=True, null=True)  # Field not required, default null
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="listings",
    )  # Field not required, default null

    # When user is deleted, the listings they created gets deleted
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_listings"
    )

    # Sets field to now when object is created = True -> cannot modify
    created_at = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)
    winner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="won_listings",
    )


class Bid(models.Model):
    amount = models.DecimalField(
        max_digits=1000, decimal_places=2, blank=False
    )  # Field is required
    bidder = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bids_placed"
    )
    bidded_on = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(
        AuctionListing, on_delete=models.CASCADE, related_name="bids"
    )


class Comment(models.Model):
    content = models.TextField(blank=False)  # Field is required

    # When user is deleted comment will stay with 'deleted user' as username
    commenter = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default="deleted user",
        related_name="commented_comments",
    )
    # Sets field to now when object is created = True -> cannot modify
    created_on = models.DateTimeField(auto_now_add=True)
    # When auction listing is deleted, all comments of that listing will be deleted
    listing = models.ForeignKey(
        AuctionListing, on_delete=models.CASCADE, related_name="comments"
    )


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    listing = models.ForeignKey(
        AuctionListing,
        on_delete=models.CASCADE,
        related_name="in_user_watchlist",
    )

    class Meta:
        unique_together = (
            "user",
            "listing",
        )
