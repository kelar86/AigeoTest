from django.db import models


class Point(models.Model):

        def __init__(self, x, y, service):
            self.x_coordinate = x
            self.y_coordinate = y
            self.service = service

search_service = models.CharField(max_length=200)
x_coordinate = models.DecimalField
y_coordinate = models.DecimalField
