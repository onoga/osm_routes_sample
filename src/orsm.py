"""orsm client
"""

import requests
try:
    from urllib import urlencode        # python2
except ImportError:
    from urllib.parse import urlencode  # python3


SERVER_URL = 'http://router.project-osrm.org'


# API: http://project-osrm.org/docs/v5.5.1/api/#requests


def call(server_url, service, profile, coordinates, **kwargs):
    url = '%s/%s/v1/%s/%s?%s' % (
        server_url,
        service,
        profile,
        ';'.join([','.join(map(str, i)) for i in coordinates]),
        urlencode(kwargs),
    )
    print "http get:", url
    return requests.get(url).json()


def route(coordinates,
    profile='driving',
    server_url=SERVER_URL,
    alternatives='false',           # Search for alternative routes and return as well.
    steps='false',                  # Return route steps for each route leg
    annotations='false',            # Returns additional metadata for each coordinate along the route geometry.
    geometries='polyline',          # polyline|polyline6|geojson, returned route geometry format (influences overview and per step)
    overview='simplified',          # simplified|full|false, add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all.
    continue_straight='default',    # default|true|false, Forces the route to keep going straight at waypoints constraining uturns there even if it would be faster. Default value depends on the profile.
):
    # if sending annotations=false have error response: "this 'annotations' param is not supported"
    kwargs = {}
    if annotations == 'true':
        kwargs['annotations'] = annotations

    return call(server_url, 'route', profile, coordinates,
        alternatives=alternatives,
        steps=steps,
        geometries=geometries,
        overview=overview,
        continue_straight=continue_straight,
        **kwargs
    )


# TODO: bearings, radiuses, hints
def service(
    service,                # One of the following values:  route ,  nearest ,  table ,  match ,  trip ,  tile
    coordinates,            # String of format  {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline})
    profile='driving',      # Mode of transportation, is determined statically by the Lua profile that is used to prepare the data using  osrm-extract . Typically car ,  bike or  foot if using one of the supplied profiles.
    server_url=SERVER_URL,  # server url
    **kwargs                # service options
):
    return eval(service)(coordinates, profile=profile, server_url=server_url, **kwargs)
