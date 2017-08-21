from map_search.models import Point
import xml.dom.minidom


def parse(response_xml, service):

    if service == 'ЕнисейГис':
        return __parse_enisey_xml(response_xml, service)
    elif service == 'YandexMap':
        return __parse_yandex_xml(response_xml, service)


def __parse_enisey_xml(response_xml, service):
    dom = xml.dom.minidom.parseString(response_xml)
    dom.normalize()
    point = dom.getElementsByTagName("geocenter")[0]
    point = point.firstChild.nodeValue
    point = point.replace("POINT", "")
    point = point.strip('()')
    points = point.split(' ')
    print(points)
    x, y = float(points[0]), float(points[1])

    return Point(x, y, service)


def __parse_yandex_xml(response_xml, service):
    dom = xml.dom.minidom.parseString(response_xml)
    dom.normalize()
    point = dom.getElementsByTagName("pos")[0]
    point = point.firstChild.nodeValue
    points = point.split(' ')

    return Point(float(points[0]), float(points[1]), service)


def check_have_result(result_xml, service):
    dom = xml.dom.minidom.parseString(result_xml)
    dom.normalize()
    if service == 'ЕнисейГис':
        results = (dom.getElementsByTagName('results')[0]).attributes['count'].value
        return int(results) > 0

    elif service == 'YandexMap':
        found = dom.getElementsByTagName('found')[0]
        results = found.firstChild.nodeValue
        return int(results) > 0

    return False
