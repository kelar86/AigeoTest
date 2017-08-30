import re
import xml.dom.minidom

import requests

from map_search.models import Point

ENISEY_BASE_URL = 'http://geo.24bpd.ru/services/service.php'
ENISEY_AUTH_KEY = '2t392pprlnfn8hgsd250gzl4'
SERVICE_NAME = 'ЕнисейГис'


def get_dom(result_xml):
    my_dom = xml.dom.minidom.parseString(result_xml)
    my_dom.normalize()
    return my_dom


def request(adress):
    auth_url = ENISEY_BASE_URL + '?api=1.03&service=auth&call=open&ukey=' + ENISEY_AUTH_KEY
    auth_req = requests.post(auth_url)
    if not auth_req.ok:
        return print("Authorization fail")
    auth_resp = auth_req.text
    skey = re.search(r'skey="(.*?)"', auth_resp).group(1)
    geo_code_url = ENISEY_BASE_URL + '?api=1.03&service=auth&call=open'
    search_resp = requests.get(geo_code_url,
                               {'api': '1.03', 'service': 'geocode', 'skey': skey, 'q': adress, 'limit': 1}).text

    return search_resp


def search_is_ok(result_xml):
    dom = get_dom(result_xml)
    results = (dom.getElementsByTagName('results')[0]).attributes['count'].value
    return int(results) > 0


def parse(response_xml):
    dom = get_dom(response_xml)
    point = dom.getElementsByTagName("geocenter")[0]
    point = point.firstChild.nodeValue
    point = point.replace("POINT", "")
    point = point.strip('()')
    points = point.split(' ')
    print(points)
    x, y = float(points[0]), float(points[1])

    return Point(x, y, SERVICE_NAME)
