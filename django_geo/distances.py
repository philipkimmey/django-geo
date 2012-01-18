import math

from geopy.distance import distance


class distances:
    @staticmethod
    def geographic_distance(lat1, lng1, lat2, lng2):
        return distance(
            (float(lat1), float(lng1),),
            (float(lat2), float(lng2),)).kilometers

    @staticmethod
    def max_variation_lat(distance):
        max_variation = abs((180 * distance) / (6371.01 * math.pi))
        return max_variation		

    @staticmethod
    def max_variation_lon(address_latitude, distance):
        top = math.sin(distance / 6371.01)
        bottom = math.cos((math.pi * address_latitude)/180)
        ratio = top / bottom
        if -1 > ratio or ratio > 1:
            max_variation = 100
        else:
            max_variation = abs(math.asin(ratio) * (180 / math.pi))
        return max_variation
