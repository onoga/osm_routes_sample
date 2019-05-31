from orsm import service
import polyline


NAME='orsm'
GEOMETRY_KEYS={'geometry'}


def get_url(points):
    return 'https://map.project-osrm.org/?z=12&center=50.444825%%2C30.591602&%s&hl=en&alt=0' % (
        '&'.join(['loc=%s%%2C%s' % (point[1], point[0]) for point in points]),
    )


def get_directions(points):
    return service('route',
        coordinates=points,
        steps='true',
        #overview='false',
        #annotations='true',
    )


def decode_polyline(geometry):
    return polyline.decode(geometry)
