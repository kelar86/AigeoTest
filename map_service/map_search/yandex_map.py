import xml.dom.minidom

import requests

from map_search.models import Point

YANDEX_BASE_URL = 'https://geocode-maps.yandex.ru/1.x/'
SERVICE_NAME = 'YandexMap'


def get_dom(result_xml):
    my_dom = xml.dom.minidom.parseString(result_xml)
    my_dom.normalize()
    return my_dom


def request(adress):
    search_resp = requests.get(YANDEX_BASE_URL, {'geocode': adress}).text
    return search_resp


def search_is_ok(result_xml):
    dom = get_dom(result_xml)
    found = dom.getElementsByTagName('found')[0]
    results = found.firstChild.nodeValue
    return int(results) > 0


def parse(response_xml):
    dom = get_dom(response_xml)
    point = dom.getElementsByTagName("pos")[0]
    point = point.firstChild.nodeValue
    points = point.split(' ')

    return Point(float(points[0]), float(points[1]), SERVICE_NAME)
