from .stock import items

MIN_QUALITY = 0


class ItemSeller(object):
    def sell(self, item):
        seller = get_seller(item.name)
        seller.sell(item)


def get_seller(item_name):
    if item_name == "Sulfuras":
        return LegendarySeller()
    else:
        return CommonSeller()


class LegendarySeller(ItemSeller):
    def sell(self, item):
        items.remove(item)
        for item in items:
            if item.name == "Sulfuras" and item.quality > MIN_QUALITY:
                item.quality -= 1


class CommonSeller(ItemSeller):
    def sell(self, item):
        items.remove(item)
