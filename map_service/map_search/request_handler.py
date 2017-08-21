import requests
import re


ENISEY_BASE_URL = 'http://geo.24bpd.ru/services/service.php'
ENISEY_AUTH_KEY = '2t392pprlnfn8hgsd250gzl4'
YANDEX_BASE_URL = 'https://geocode-maps.yandex.ru/1.x/'


def __req_yandex(adress):
    search_resp = requests.get(YANDEX_BASE_URL, {'geocode': adress}).text
    return search_resp


def __req_enisey(adress):
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


def request(adress, service):
    if service == "ЕнисейГис":
        return __req_enisey(adress)
    elif service == "YandexMap":
        return __req_yandex(adress)
