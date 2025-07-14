class Item:
    MIN_QUALITY = 0
    MAX_QUALITY = 50

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in     
        self.quality = quality     

    @property
    def sell_in(self):
        return self._sell_in

    @sell_in.setter
    def sell_in(self, value):
        if not isinstance(value, int):
            raise TypeError("sell_in must be an integer.")
        self._sell_in = value

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        if not isinstance(value, int):
            raise TypeError("quality must be an integer.")
        
        #Règle spéciale pour Sulfuras : qualité doit être **exactement 80**
        if self.name == "Sulfuras, Hand of Ragnaros":
            if value != 80:
                raise ValueError("Sulfuras must have a quality of exactly 80.")
        else:
            if not (self.MIN_QUALITY <= value <= self.MAX_QUALITY):
                raise ValueError(
                    f"quality must be between {self.MIN_QUALITY} and {self.MAX_QUALITY}."
                )
        
        self._quality = value

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
