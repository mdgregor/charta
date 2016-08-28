import math

RADIUS_OF_EARTH = 6378.1

def directional_point(gps_point, bearing):

    DISTANCE = .03

    lat1 = math.radians(gps_point[0])
    lon1 = math.radians(gps_point[1])

    lat2 = math.asin(math.sin(lat1) * math.cos(DISTANCE / RADIUS_OF_EARTH) +
                         math.cos(lat1) * math.sin(DISTANCE / RADIUS_OF_EARTH) * math.cos(bearing))

    lon2 = lon1 + math.atan2(math.sin(bearing) * math.sin(DISTANCE / RADIUS_OF_EARTH) * math.cos(lat1),
                                 math.cos(DISTANCE / RADIUS_OF_EARTH) - math.sin(lat1) * math.sin(lat2))

    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)

    return lat2, lon2


def bearing_between_two_points(gps1, gps2):
    lat1 = math.radians(gps1[0])
    lat2 = math.radians(gps2[0])

    diffLong = math.radians(gps2[1] - gps1[1])

    y = math.sin(diffLong) * math.cos(lat2)
    x = (math.cos(lat1) * math.sin(lat2)) - (math.sin(lat1) * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.degrees(math.atan2(y, x))
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing


def distance_between_two_points(gps1, gps2):
    lat1 = math.radians(gps1[0])
    lat2 = math.radians(gps2[0])
    dlon = math.radians(gps2[1] - gps1[1])
    dlat = math.radians(gps2[0] - gps1[0])
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = c * RADIUS_OF_EARTH

    return distance * 1000


def main():

    gps_point_start = (47.438933, -122.243732)
    gps_point_end = (47.463129, -122.241822)

    distance = distance_between_two_points(gps_point_start, gps_point_end)
    bearing = bearing_between_two_points(gps_point_start, gps_point_end)

    number_of_points = int(distance / 30)

    gps_points = [gps_point_start]
    for x in range(number_of_points):
        gps_points.append(directional_point(gps_points[x], bearing))
        x += 1
    pass

if __name__ == "__main__":
    main()
