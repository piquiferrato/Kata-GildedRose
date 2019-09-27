class GuildedRose(object):

    def update_items(self, items, updater):
        for item in items:
            updater.update(item)

    def sell_item(self, item, seller):
        seller.sell(item)