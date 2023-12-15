class SpaceAge:

    def __init__(self, seconds):
        self.age = seconds / 31557600

    def on_mercury(self):
        return self.year(0.2408467)

    def on_venus(self):
        return self.year(0.61519726)

    def on_earth(self):
        return self.year(1)

    def on_mars(self):
        return self.year(1.8808158)

    def on_jupiter(self):
        return self.year(11.862615)

    def on_saturn(self):
        return self.year(29.447498)

    def on_uranus(self):
        return self.year(84.016846)

    def on_neptune(self):
        return self.year(164.79132)

    def year(self, orbit):
        return round(self.age / orbit, 2)
