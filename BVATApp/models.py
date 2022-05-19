# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Woord(models.Model):
    id = models.AutoField(primary_key=True)
    woord = models.TextField(blank=True, null=True)
    taal = models.TextField(blank=True, null=True)
    moeilijkheidsgraad = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        unique_together = ('woord', 'taal')
        db_table = 'Woord'

    def __str__(self):
        return '%s / %s / %s' % (self.woord, self.taal, self.moeilijkheidsgraad)


class Highscore(models.Model):
    id = models.AutoField(primary_key=True)
    naam = models.TextField(blank=True, null=True)
    wpm = models.IntegerField(blank=True, null=True)
    fouten = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    moeilijkheidsgraad = models.TextField(blank=True, null=True)
    taal = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Highscore'

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.id, self.naam, self.wpm, self.fouten, self.score)