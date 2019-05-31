# coding: utf-8
import json
import webbrowser
import helpers
import sample_openrouteservice
import sample_orsm
import sample_graphhopper
from time import time


SERVICES = [
    sample_openrouteservice,
    sample_orsm,
    sample_graphhopper,
]


points = map(lambda x: (x[1], x[0]), [
    (50.405528, 30.680170),  # kasta store
    (50.514715, 30.433187),  # ул. Светлицкого, 22
    (50.443214, 30.531506),  # ул. Шелковичная, 17/2
])

def main():
    for service in SERVICES:
        print "===========", service.NAME

        t = time()
        result = service.get_directions(points)
        dt = time() - t

        print "directions request complete in %.3f seconds" % (dt,)

        helpers.decode_geometry(result, service.decode_polyline, service.GEOMETRY_KEYS)

        filename = "%s.json" % service.NAME
        open(filename, 'w').write(json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True).encode('UTF-8'))
        print "response saved to", filename


    for service in SERVICES:
        url = service.get_url(points)
        print "opening browser:", url
        webbrowser.open(url)


if __name__ == '__main__':
    main()
