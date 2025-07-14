from updaters import (
    NormalItemUpdater,
    AgedBrieUpdater,
    SulfurasUpdater,
    BackstagePassUpdater,
    ConjuredItemUpdater,
)

class UpdaterFactory:
    def get_updater(self, item):
        if item.name == "Aged Brie":
            return AgedBrieUpdater()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater()
        elif item.name.startswith("Conjured"):
            return ConjuredItemUpdater()
        else:
            return NormalItemUpdater()