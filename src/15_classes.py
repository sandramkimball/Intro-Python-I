# Make a class LatLon that can be passed parameters `lat` and `lon` to the constructor
class LatLon(lat, lon):
    let = 0
    lon = 0
    def _init_(self):

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class waypoint(name, LatLon):
    name = ''
    def _init_(self):
        super()

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class geocache(difficulty, size, Waypoint):
    difficulty = 0
    size = 0
    def _init_(self):
        super()

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint('Catacombs', 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print( waypoint._str_() )

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print( geocache._str_() )
