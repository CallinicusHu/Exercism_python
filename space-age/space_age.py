class SpaceAge:
    def __init__(self, seconds):
        self.age = seconds / 31557600

    def on_mercury(sec):
        return round(sec.age / 0.2408467, 2)

    def on_venus(sec):
        return round(sec.age / 0.61519726, 2)

    def on_earth(sec):
        return round(sec.age, 2)

    def on_mars(sec):
        return round(sec.age / 1.8808158, 2)

    def on_jupiter(sec):
        return round(sec.age / 11.862615, 2)

    def on_saturn(sec):
        return round(sec.age / 29.447498, 2)

    def on_uranus(sec):
        return round(sec.age / 84.016846, 2)

    def on_neptune(sec):
        #return year(seconds, 164.79132) # year unreachable!
        return round(sec.age / 164.79132, 2)

    def year(sec, orbit):
        return round(sec.age / orbit, 2)
        #orbit would be for example 164.79132 for Jupiter and I just want to call year planet(seconds, the-value-of-orbit) but my functions are unreachable for each other and I don't understand how to solve this. I guess it is because of class
        #it is probably something to do with what the doc called as global but I don't understand