MAX_QUALITY_LIMIT = 50
MIN_QUALITY_LIMIT = 0
MIN_SELLIN_VALUE = 0


class Item(object):
    def __init__(self, name, quality, sellin_value):
        self.name = name
        self.quality = quality
        self.sellin_value = sellin_value

    @property
    def quality(self):
        return self.__quality

    @quality.setter
    def quality(self, value):
        if value > MAX_QUALITY_LIMIT or value < MIN_QUALITY_LIMIT:
            raise ValueError("quality must be between %s - %s" % (MAX_QUALITY_LIMIT, MIN_QUALITY_LIMIT))

        self.__quality = value

    @property
    def sellin_value(self):
        return self.__sellin_value

    @sellin_value.setter
    def sellin_value(self, value):
        if value < MIN_SELLIN_VALUE:
            raise ValueError("quality must not be negative")

        self.__sellin_value = value
