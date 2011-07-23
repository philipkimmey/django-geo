import math
class distances:
	@staticmethod
	def geographic_distance(lat1, lng1, lat2, lng2):
        lat1 = float(lat1)
        lng1 = float(lng1)
        lat2 = float(lat2)
        lng2 = float(lng2)
		lat1 = (lat1 * math.pi) / 180
		lng1 = (lng1 * math.pi) / 180
		lat2 = (lat2 * math.pi) / 180
		lng2 = (lng2 * math.pi) / 180
		a = (math.sin(lat1)*math.sin(lat2))+(math.cos(lat1)*math.cos(lat2)*math.cos(lng2 - lng1))
		return math.acos(a) * 6371.01

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

