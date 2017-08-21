from map_search import request_handler
from map_search import response_parser

MAP_SERVICES = ["ЕнисейГис", "YandexMap"]


def search(adress):
    for service in MAP_SERVICES:
        srch = request_api(adress, service)

        if search_is_ok(srch, service):
            result = get_coordinate(srch, service)
            if result is not None:
                return result
    return None


def request_api(adress, service):
    return request_handler.request(adress, service)


def search_is_ok(result_xml, service):
    return response_parser.check_have_result(result_xml, service)


def get_coordinate(response_xml, service):
    return response_parser.parse(response_xml, service)

