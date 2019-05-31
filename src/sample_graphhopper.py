import graphhopper
import polyline

NAME='graphhopper'
GEOMETRY_KEYS={'points','snapped_waypoints'}
API_KEY='e70827eb-c949-496d-b203-0d205865fe99'


def get_url(coordinates):
    return 'https://graphhopper.com/maps/?%s&locale=en-US&vehicle=car&weighting=fastest&elevation=true&use_miles=false&layer=Omniscale' % (
        '&'.join(['point=%s%%2C%s' % (i[1], i[0]) for i in coordinates]),
    )


def get_directions(coordinates):
    return graphhopper.call(API_KEY, 'route', coordinates)


def decode_polyline(geometry):
    return polyline.decode(geometry)
