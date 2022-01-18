from django.db import models


# Create your models here.

class LineA(models.Model):
    shift_model = models.IntegerField()
    std_shift_time = models.IntegerField()
    total_break_time_gross = models.IntegerField()
    start_up = models.IntegerField()
    t_break = models.IntegerField()
    lunch = models.IntegerField()
    others = models.IntegerField()
    std_shift_time_net = models.IntegerField()
    days_or_week = models.IntegerField()
    week_or_year = models.IntegerField()
