from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Players(models.Model):
    name = models.CharField(max_length = 50)
    gold = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

class Characters(models.Model):
    char_class = models.CharField(max_length = 50)
    char_level = models.IntegerField()
    maxHealth = models.IntegerField()
    # maxMana = models.IntegerField()
    # minDam = models.IntegerField()
    # maxDam = models.IntegerField()
    # mdamage = models.IntegerField()
    # defense = models.IntegerField()
    # evasion = models.IntegerField()
    # delay:TimeInterval = models.IntegerField()
    # experience = models.IntegerField()
