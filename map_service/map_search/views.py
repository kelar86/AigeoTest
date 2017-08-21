from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader

from map_search import search_manager
from map_search.models import Point


def index(req):
    template = loader.get_template('map_service/index.html')
    return HttpResponse(template.render())


def search(req):
    if 'adress' in req.GET:

        adress = req.GET['adress']
        point = search_manager.search(adress)

        if isinstance(point, Point):
            return render_to_response('map_service/search.html', {'x': point.x_coordinate,
                                                                  'y': point.y_coordinate,
                                                                  'service': point.service})
        else:
            return HttpResponse(adress + " Адрес не найден")

    else:
        return HttpResponse('You submitted an empty form.')
