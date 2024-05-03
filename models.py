class NearEarthObject:
    def __init__(self, designation, name, diameter=None, hazardous=None):
        self.designation = designation
        self.name = name
        self.diameter = diameter
        self.hazardous = hazardous

    def __str__(self):
        return f"{self.designation}: {self.name}, Diameter: {self.diameter} km, Hazardous: {self.hazardous}"

    def serialize(self):
        return {
            'designation': self.designation,
            'name': self.name if self.name else "",
            'diameter_km': self.diameter if self.diameter else float('nan'),
            'potentially_hazardous': bool(self.hazardous)
        }


class CloseApproach:
    def __init__(self, time, distance, velocity, neo):
        self.time = time
        self.distance = distance
        self.velocity = velocity
        self.neo = neo

    def __str__(self):
        return f"At {self.time}, {self.neo} approached Earth at a distance of {self.distance} AU with a velocity of {self.velocity} km/s"

    def serialize(self):
        return {
            'datetime_utc': str(self.time),
            'distance_au': self.distance,
            'velocity_km_s': self.velocity,
            'neo': self.neo.serialize()
        }
