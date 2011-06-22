from decimal import Decimal

from django.test import TestCase

from . import Point
from . import Bounds

class PointTest(TestCase):
    def setUp(self):
        self.point1 = Point(47.2422, -122.245)
        self.point2 = Point('47.2422', '-122.245')
        self.point3 = Point('47.2455', '-122.245')
        self.point4 = Point(47.2422, '-122.240')
    def test_args_kwargs(self):
        point1 = Point(47.2422, -122.245)
        point2 = Point('47.2422', '-122.245')
        self.assertEqual(Decimal('47.2422'), point1.lat)
        self.assertEqual(Decimal('47.2422'), point2.latitude)
        point3 = Point(lat=unicode('47.2422'), lng=unicode('-122.245'))
        point4 = Point(latitude='47.2422', longitude='-122.245')
        self.assertEqual(point3.latitude, point4.latitude)
        self.assertRaises(Exception, Point, latitude='42.00')
    def test_eq(self):
        self.assertEqual(self.point1, self.point2)
        self.assertNotEqual(self.point1, self.point3)
        self.assertNotEqual(self.point1, self.point4)
    def test_hash(self):
        self.assertEqual(hash(self.point1), hash(self.point2))
        self.assertNotEqual(hash(self.point1), hash(self.point3))
        self.assertNotEqual(hash(self.point1), hash(self.point4))
    def test_valid_values(self):
        self.assertRaises(Exception, Point, -90.2, -122.42)
        self.assertRaises(Exception, Point, 90.1, -122.45)
        self.assertRaises(Exception, Point, 45, -181)
        self.assertRaises(Exception, Point, 42, 181)

class BoundsTest(TestCase):
    def setUp(self):
        sw1 = Point(47.244, -122.42)
        ne1 = Point(48.244, -121.24)
        self.bounds1 = Bounds(sw1, ne1)
        sw2 = Point(47.244, -122.42)
        ne2 = Point(48.244, -121.24)
        self.bounds2 = Bounds(sw2, ne2)
        sw3 = Point(45.55, -122.01)
        ne3 = Point(48.00, -120.42)
        self.bounds3 = Bounds(sw3, ne3)
    def test_bounds_eq(self):
        self.assertEqual(self.bounds1, self.bounds2)
        self.assertNotEqual(self.bounds1, self.bounds3)
    def test_hash(self):
        self.assertEqual(hash(self.bounds1), hash(self.bounds2))
        self.assertNotEqual(hash(self.bounds1), hash(self.bounds3))
        
