from domain.entities.item import Item
from domain.entities.gilded_rose import GuildedRose
from domain.entities.stock import items as item_stock
from domain.entities.item_updater import ItemUpdater
from domain.entities.item_seller import ItemSeller

store = GuildedRose()
updater = ItemUpdater()
seller = ItemSeller()

for item in item_stock:
    print(item.name, "quality: %s" % item.quality, "sellin_value: %s" % item.sellin_value)
    print("______________________________________________________________________________")

store.update_items(item_stock, updater)
store.update_items(item_stock, updater)
store.update_items(item_stock, updater)

for item in item_stock:
    print(item.name, "quality: %s" % item.quality, "sellin_value: %s" % item.sellin_value)

store.sell_item(item_stock[0], seller)

for item in item_stock:
    print(item.name, "quality: %s" % item.quality, "sellin_value: %s" % item.sellin_value)
    print("______________________________________________________________________________")