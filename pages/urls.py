from django.urls import path

from .views import HomePageView, ShopBrowserPageView, ShopDetailsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("shop_browser", ShopBrowserPageView.as_view(), name="shop_browser"),
    path("shop_details", ShopDetailsPageView.as_view(), name="shop_details"),
]
