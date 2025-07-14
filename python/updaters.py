class ItemUpdater:
    MIN_QUALITY = 0
    MAX_QUALITY = 50

    def update(self, item):
        pass

    def increase_quality(self, item, amount=1):
        item.quality = min(item.quality + amount, self.MAX_QUALITY)

    def decrease_quality(self, item, amount=1):
        item.quality = max(item.quality - amount, self.MIN_QUALITY)

    def decrease_sell_in(self, item):
        item.sell_in -= 1


class NormalItemUpdater(ItemUpdater):
    def update(self, item):
        self.decrease_quality(item, 1 if item.sell_in > 0 else 2)
        self.decrease_sell_in(item)


class AgedBrieUpdater(ItemUpdater):
    def update(self, item):
        self.increase_quality(item, 1 if item.sell_in > 0 else 2)
        self.decrease_sell_in(item)


class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass  # Legendary item does not change


class BackstagePassUpdater(ItemUpdater):
    def update(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            self.increase_quality(item, 3)
        elif item.sell_in <= 10:
            self.increase_quality(item, 2)
        else:
            self.increase_quality(item, 1)
        self.decrease_sell_in(item)


class ConjuredItemUpdater(ItemUpdater):
    def update(self, item):
        self.decrease_quality(item, 2 if item.sell_in > 0 else 4)
        self.decrease_sell_in(item)