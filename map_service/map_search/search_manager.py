from map_search import enisey_gis
from map_search import yandex_map

MAP_SERVICES = [enisey_gis, yandex_map]


def search(adress):
    for service in MAP_SERVICES:

        srch = service.request(adress)

        if service.search_is_ok(srch):
            result = service.parse(srch)
            if result is not None:
                return result
    return None

