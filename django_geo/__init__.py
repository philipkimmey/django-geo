from decimal import Decimal
from distances import distances

class Point(object):
    """
    Two-tuple of lat/lng.
    Stored as Decimal.
    """
    def __hash__(self):
        return (hash(self.lat) * 179) ^ hash(self.lng)
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.lat != other.lat:
            return False
        if self.lng != other.lng:
            return False
        return True
    def __ne__(self, other):
        return not (self == other)
    def __init__(self, *args, **kwargs):
        if 'lat' in kwargs and 'lng' in kwargs:
            self.lat = Decimal(unicode(kwargs.pop('lat')))
            self.lng = Decimal(unicode(kwargs.pop('lng')))
        elif 'latitude' in kwargs and 'longitude' in kwargs:
            self.lat = Decimal(unicode(kwargs.pop('latitude')))
            self.lng = Decimal(unicode(kwargs.pop('longitude')))
        elif len(args) == 2:
            self.lat = Decimal(unicode(args[0]))
            self.lng = Decimal(unicode(args[1]))
        else:
            raise Exception("Invalid constructor params to Point")
        if self.lat > Decimal('90.0') or self.lat < Decimal('-90.0'):
            raise Exception("Invalid latitude value")
        if self.lng > Decimal('180.0') or self.lng < Decimal('-180.0'):
            raise Exception("Invalid longitude value")
        super(Point, self).__init__()
    @property
    def latitude(self):
        """
        Alternate accessor to lat.
        """
        return self.lat
    @property
    def longitude(self):
        """
        Alternate accessor to lng.
        """
        return self.lng

class Bounds(object):
    """
    Effectively two-tuple of Point objects.
    Takes args as sw Point and ne Point,
    Also will accept them as sw=Point,
    ne=Point
    """
    def __hash__(self):
        hsh = 0
        hsh = hash(self.sw) * 127
        hsh = hsh ^ hash(self.ne)
        return hsh
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.sw != other.sw:
            return False
        if self.ne != other.ne:
            return False
        return True
    def __ne__(self, other):
        return not (self == other)
    def __init__(self, *args, **kwargs):
        if 'sw' in kwargs and 'ne' in kwargs:
            # sw & ne points provided
            self.sw = kwargs.pop('sw')
            self.ne = kwargs.pop('ne')
        elif len(args) == 2:
            # sw & ne points provided as args
            self.sw = args[0]
            self.ne = args[1]
        elif len(kwargs) == 4:
            # kwargs minlat, minlng, maxlat, maxlng
            self.sw = Point(kwargs.pop('minlat'), kwargs.pop('minlng'))
            self.ne = Point(kwargs.pop('maxlat'), kwargs.pop('maxlng'))
        # make sure sw is more southwesterly
        # empty bounds is valid, so do > not =>
        if (self.sw.lat > self.ne.lat) or (self.sw.lng > self.ne.lng):
            raise Exception("Points are not in (sw, ne) order")
        super(Bounds, self).__init__()
    def get_radius(self):
        approx_distance = distances.geographic_distance(
                self.sw.lat, self.sw.lng,
                self.ne.lat, self.ne.lng)
        return approx_distance / 2
