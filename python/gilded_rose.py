# -*- coding: utf-8 -*-

from factory import UpdaterFactory

class GildedRose:
    def __init__(self, items):
        self.items = items
        self.factory = UpdaterFactory()

    def update_quality(self):
        for item in self.items:
            updater = self.factory.get_updater(item)
            updater.update(item)

