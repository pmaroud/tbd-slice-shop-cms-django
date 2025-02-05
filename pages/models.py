import dateutil.parser


class Shop:
    def __init__(self, payload):
        self.id = payload["shop_id"]
        self.name = payload.get("name")
        self.member_since = str(dateutil.parser.isoparse(payload["created_at"]).date())
        self.full_address = ", ".join([payload["address"], payload["city"], f"{payload["state"]} {payload["zipcode"]}"])
        self.phone = payload.get("phone", "Not provided")
