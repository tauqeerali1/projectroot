class DateFilter:
    def __init__(self, date):
        self.date = date

    def __call__(self, approach):
        return approach.time.date() == self.date


class DistanceFilter:
    def __init__(self, min_distance, max_distance):
        self.min_distance = min_distance
        self.max_distance = max_distance

    def __call__(self, approach):
        return self.min_distance <= approach.distance <= self.max_distance


class VelocityFilter:
    def __init__(self, min_velocity, max_velocity):
        self.min_velocity = min_velocity
        self.max_velocity = max_velocity

    def __call__(self, approach):
        return self.min_velocity <= approach.velocity <= self.max_velocity


class DiameterFilter:
    def __init__(self, min_diameter, max_diameter):
        self.min_diameter = min_diameter
        self.max_diameter = max_diameter

    def __call__(self, approach):
        return self.min_diameter <= approach.neo.diameter <= self.max_diameter


class HazardousFilter:
    def __init__(self, hazardous):
        self.hazardous = hazardous

    def __call__(self, approach):
        return approach.neo.hazardous == self.hazardous
