# Recréons les fichiers après le reset

# Définir la classe Item
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


# Implémenter les classes de mise à jour des objets
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
        pass


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


# Implémenter la classe GildedRose
class GildedRose:
    def __init__(self, items):
        self.items = items
        self.factory = UpdaterFactory()

    def update_quality(self):
        for item in self.items:
            updater = self.factory.get_updater(item)
            updater.update(item)


# Implémenter la factory pour créer des items facilement
class ItemFactory:
    def create(self, name, sell_in, quality):
        return Item(name, sell_in, quality)


# Tests unitaires
import unittest

class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        self.item_factory = ItemFactory()

    def test_regular_quality(self):
        items = [self.item_factory.create("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(39, items[0].quality)

    def test_regular_sell_in(self):
        items = [self.item_factory.create("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].sell_in)

    def test_regular_sell_in_passed(self):
        items = [self.item_factory.create("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(38, items[0].quality)

    def test_aged_brie_quality(self):
        items = [self.item_factory.create("Aged Brie", 10, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_sulfuras_quality_unvariated(self):
        items = [self.item_factory.create("Sulfuras, Hand of Ragnaros", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(40, items[0].quality)

    def test_backstage_quality_double_increase(self):
        items = [self.item_factory.create("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(42, items[0].quality)

    def test_conjured_quality(self):
        items = [self.item_factory.create("Conjured Mana Cake", 6, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


# Exécution des tests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(GildedRoseTest))
