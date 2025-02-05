import requests

from .models import Shop


def fetch_shop(id) -> Shop:
    url = f"https://shop-cms.private.qa.slicelife.com/consumer-api/v1/shops/{id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Shop(response.json()["shop"])

    except requests.exceptions.HTTPError:
        # Handle specific HTTP errors
        if response.status_code == 404:
            return None
