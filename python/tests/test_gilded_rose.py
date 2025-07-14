# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose
from item import Item

class GildedRoseTest(unittest.TestCase):
    def test_normal_item_quality(self):
        items = [Item("bread", 10, 20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 19)

    def test_normal_item_sell_in(self):
        items = [Item("bread", 10, 20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].sell_in, 9)

    def test_normal_item_quality_expired(self):
        items = [Item("bread", 0, 10)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 8)

    def test_aged_brie_increase(self):
        items = [Item("Aged Brie", 5, 10)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 11)

    def test_aged_brie_quality_max(self):
        items = [Item("Aged Brie", 5, 50)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_sulfuras_no_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)

    def test_backstage_pass_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_backstage_pass_increase_double(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_backstage_pass_increase_triple(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 23)

    def test_backstage_pass_expired(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_conjured_item(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 4)

    def test_conjured_item_expired(self):
        items = [Item("Conjured Mana Cake", 0, 6)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 2)


if __name__ == '__main__':
    unittest.main()
