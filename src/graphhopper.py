"""graphhopper client
"""

import requests

try:
    from urllib import urlencode  # python2
except ImportError:
    from urllib.parse import urlencode  # python3


SERVER_URL = 'https://graphhopper.com'


# https://docs.graphhopper.com/#operation/getRoute

def call(
    api_key,
    service,
    points,
    server_url=SERVER_URL,
    **kwargs
):
    kwargs['key'] = api_key
    url = '%s/api/1/%s?%s&%s' % (
        server_url,
        service,
        '&'.join(['point=%s,%s' % (i[1], i[0]) for i in points]),
        urlencode(kwargs),
    )
    print "http get", url
    return requests.get(url).json()
