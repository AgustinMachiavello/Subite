"""Model route"""

# Models
from django.db import models


class Route(models.Model):
    user = models.ForeignKey('accounts.User', null=True,on_delete=models.CASCADE)
    start_point_lat = models.FloatField(null=False, default=0)
    start_point_lon = models.FloatField(null=False, default=0)
    end_point_lat = models.FloatField(null=False, default=0)
    end_point_lon = models.FloatField(null=False, default=0)

    def __str__(self):
        return "(lat,lon) ({0},{1}) to ({2}, {3}) ID:{4}".format(
            self.start_point_lat, 
            self.start_point_lon,
            self.end_point_lat,
            self.end_point_lon,
            self.id,
            )

class Point(models.Model):
    route = models.ForeignKey('maps.Route', null=True, on_delete=models.CASCADE)
    lat = models.FloatField(null=False, default=0)
    lon = models.FloatField(null=False, default=0)

    def __str__(self):
        return "({0}, {1})".format(self.lat, self.lon)