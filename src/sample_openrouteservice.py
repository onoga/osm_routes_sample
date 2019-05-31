import openrouteservice
from openrouteservice.directions import directions
import json

# API https://openrouteservice-py.readthedocs.io/en/latest/openrouteservice.html

NAME = 'openrouteservice'
GEOMETRY_KEYS={'geometry'}
API_KEY='5b3ce3597851110001cf624865fe880a162d42ba88ef1973c8a0b2e7'


def get_url(points, route_pref='recommended'):
    return 'https://maps.openrouteservice.org/directions?n1=50.432142&n2=30.550232&n3=12&a=%s&b=0&c=%d&k1=en-US&k2=km' % (
        ','.join(['%s,%s' % (point[1], point[0]) for point in points]),
        {'fastest':0, 'shortest':1, 'recommended': 2}[route_pref],
    )


def get_directions(points):

    client = openrouteservice.Client(key=API_KEY)
    kwargs = {
        'profile': 'driving-car',
        #'extra_info': ['steepness', 'suitability', 'surface', 'waycategory', 'waytype', 'tollways', 'traildifficulty', 'roadaccessrestrictions'],
        #'elevation': True,
    }

    #print "REQUEST"
    #directions(client, points, dry_run=True, **kwargs)

    result = directions(client, points, **kwargs)

    #print "RESPONSE"
    #print json.dumps(result, indent=4, ensure_ascii=False, sort_keys=True)

    #for i, route in enumerate(result['routes']):
    #    print "ROUTE #%s" % i
    #    waypoints = openrouteservice.convert.decode_polyline(route['geometry'], is3d=False)['coordinates']
    #    print "\twaypoints count=%s: %s" % (len(waypoints), waypoints)
    #    for segment in route['segments']:
    #        for j, step in enumerate(segment['steps']):
    #            print "\tstep %s: %s" % (j, step['instruction'])

    return result


def decode_polyline(geometry):
    return openrouteservice.convert.decode_polyline(geometry, is3d=False)['coordinates']
