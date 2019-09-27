MAX_QUALITY = 50
MIN_QUALITY = 0
MIN_SELLIN_VALUE = 0


class ItemUpdater(object):
    def update(self, item):
        updater = get_updater(item.name)
        updater.update(item)


def get_updater(item_name):
    if item_name == "Aged Brie":
        return IncreaseQualityByDay()

    elif item_name == "BackStage Passes":
        return LimitedTime()

    elif item_name == "Conjured":
        return Conjured()

    elif item_name == "Sulfuras":
        return Legendary()

    else:
        return DecreaseQualityByDay()


class IncreaseQualityByDay(ItemUpdater):
    def update(self, item):
        quality = item.quality

        if quality == MAX_QUALITY:
            quality = MAX_QUALITY

        if quality < MAX_QUALITY:
            quality += 1

        item.quality = quality
        item.sellin_value = get_updated_sellin_value(item.sellin_value)


class DecreaseQualityByDay(ItemUpdater):
    def update(self, item):
        quality = item.quality
        sellin_value = item.sellin_value

        if quality == MIN_QUALITY:
            item.quality = MIN_QUALITY

        if sellin_value == MIN_SELLIN_VALUE and quality >= MIN_QUALITY + 2:
            quality -= 2

        else:
            quality -= 1

        if quality < MIN_QUALITY:
            quality = MIN_QUALITY

        item.quality = quality
        item.sellin_value = get_updated_sellin_value(item.sellin_value)


class LimitedTime(ItemUpdater):
    def update(self, item):
        quality = item.quality
        sellin_value = item.sellin_value

        if quality == MAX_QUALITY and sellin_value != MIN_SELLIN_VALUE:
            quality = MAX_QUALITY

        elif sellin_value == MIN_SELLIN_VALUE:
            quality = 0

        elif sellin_value <= 5:
            quality += 3

        elif sellin_value <= 10:
            quality += 2

        if quality > MAX_QUALITY:
            item.quality = MAX_QUALITY

        item.quality = quality
        item.sellin_value = get_updated_sellin_value(item.sellin_value)


class Conjured(ItemUpdater):
    def update(self, item):
        quality = item.quality

        if quality == MIN_QUALITY:
            quality = MIN_QUALITY

        if quality - 2 < MIN_QUALITY:
            quality = MIN_QUALITY

        else:
            quality -= 2

        item.quality = quality
        item.sellin_value = get_updated_sellin_value(item.sellin_value)


class Legendary(ItemUpdater):
    def update(self, item):
        item.sellin_value = get_updated_sellin_value(item.sellin_value)


def get_updated_sellin_value(sellin_value):
    sellin_value -= 1

    if sellin_value < MIN_SELLIN_VALUE:
        return MIN_SELLIN_VALUE

    return sellin_value
