# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose
from item import Item

class GildedRoseTest(unittest.TestCase):

    # Test 1 : Les objets normaux perdent 1 de qualité chaque jour
    def test_normal_item_quality(self):
        items = [Item("bread", 10, 20)]  # sell_in > 0, qualité = 20
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 19)  # qualité doit diminuer de 1

    # Test 2 : Les objets normaux perdent 1 jour de sell_in chaque jour
    def test_normal_item_sell_in(self):
        items = [Item("bread", 10, 20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].sell_in, 9)  # sell_in doit diminuer de 1

    # Test 3 : Une fois la date passée (sell_in <= 0), la qualité diminue deux fois plus vite
    def test_normal_item_quality_expired(self):
        items = [Item("bread", 0, 10)]  # item expiré
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 8)  # qualité -2

    # Test 4 : Aged Brie augmente en qualité chaque jour
    def test_aged_brie_increase(self):
        items = [Item("Aged Brie", 5, 10)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 11)  # qualité +1

    # Test 5 : La qualité ne dépasse jamais 50, même pour Aged Brie
    def test_aged_brie_quality_max(self):
        items = [Item("Aged Brie", 5, 50)]  # déjà à la qualité max
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 50)  # ne doit pas augmenter

    # Test 6 : Sulfuras ne change jamais, ni en qualité, ni en sell_in
    def test_sulfuras_no_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 80)  # qualité fixe
        self.assertEqual(items[0].sell_in, 0)   # sell_in fixe aussi

    # Test : Vérifie qu'une exception est levée si on crée un objet Sulfuras avec une qualité ≠ 80
    def test_sulfuras_with_invalid_quality(self):
        # On attend une exception de type ValueError lorsque la qualité n'est pas 80
        with self.assertRaises(ValueError) as context:
            # Création d'un objet Sulfuras avec une qualité invalide (90 au lieu de 80)
            Item("Sulfuras, Hand of Ragnaros", 0, 90)
        
        # Vérifie que le message de l'exception contient bien l'explication attendue
        self.assertIn("Sulfuras must have a quality of exactly 80", str(context.exception))

    # Test 7 : Backstage pass augmente de +1 quand il reste > 10 jours
    def test_backstage_pass_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 21)

    # Test 8 : Backstage pass augmente de +2 quand il reste entre 6 et 10 jours
    def test_backstage_pass_increase_double(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 22)

    # Test 9 : Backstage pass augmente de +3 quand il reste 5 jours ou moins
    def test_backstage_pass_increase_triple(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 23)

    # Test 10 : Backstage pass tombe à 0 après la date du concert (sell_in <= 0)
    def test_backstage_pass_expired(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 0)

    # Test 11 : Les objets "Conjured" se dégradent deux fois plus vite que les objets normaux
    def test_conjured_item(self):
        items = [Item("Conjured Mana Cake", 3, 6)]  # non expiré
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 4)  # qualité -2

    # Test 12 : Les objets "Conjured" expirés se dégradent 4 fois plus vite (-4 par jour)
    def test_conjured_item_expired(self):
        items = [Item("Conjured Mana Cake", 0, 6)]  # expiré
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(items[0].quality, 2)  # qualité -4

# Exécution des tests unitaires
if __name__ == '__main__':
    unittest.main()
