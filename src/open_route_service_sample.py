import openrouteservice
from openrouteservice.directions import directions
import json

# API https://openrouteservice-py.readthedocs.io/en/latest/openrouteservice.html

API_KEY='5b3ce3597851110001cf624865fe880a162d42ba88ef1973c8a0b2e7'

points = [
    # NOTE: reversed, (lon, lat)
    (30.6794, 50.4052),
    (30.5217, 50.4489),
    (30.6235, 50.3628),
]



client = openrouteservice.Client(key=API_KEY)
kwargs = {
    'profile': 'driving-car',
    #'extra_info': ['steepness', 'suitability', 'surface', 'waycategory', 'waytype', 'tollways', 'traildifficulty', 'roadaccessrestrictions'],
    'elevation': True,
}

print "REQUEST"
directions(client, points, dry_run=True, **kwargs)

result = directions(client, points, **kwargs)

print "RESPONSE"
print json.dumps(result, indent=4, ensure_ascii=False, sort_keys=True)

for i, route in enumerate(result['routes']):
    print "ROUTE #%s" % i
    waypoints = openrouteservice.convert.decode_polyline(route['geometry'], is3d=True)['coordinates']
    print "\twaypoints count=%s: %s" % (len(waypoints), waypoints)
    for segment in route['segments']:
        for j, step in enumerate(segment['steps']):
            print "\tstep %s: %s" % (j, step['instruction'])
