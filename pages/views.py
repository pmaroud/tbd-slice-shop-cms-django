
from django.views.generic import TemplateView

from pages.services import fetch_shop


class HomePageView(TemplateView):
    template_name = "home.html"


class ShopDetailsPageView(TemplateView):
    template_name = "_partials/shop_results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop_id = self.request.GET.get("id", "")
        context["shop_id"] = shop_id
        if shop_id:
            shop_data = fetch_shop(shop_id)
            context.update({"shop_found": bool(shop_data), "shop": shop_data})
        return context


class ShopBrowserPageView(TemplateView):
    template_name = "shop_browser.html"
