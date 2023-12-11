from django.db import models
from django.contrib.auth.models import User
from apps.authentication.models import *


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "Events"

class Athlete(models.Model):
    
    id=models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=500)
    lastName = models.CharField(max_length=500)
    email = models.CharField(max_length=500, blank=True, null=True, default=None)
    phone = models.CharField(max_length=500, blank=True, null=True, default=None)
    
    parent_id = models.CharField(max_length=500, blank=True, null=True, default=None)
    parent_firstName = models.CharField(max_length=500, blank=True, null=True, default=None)
    parent_lastName = models.CharField(max_length=500, blank=True, null=True, default=None)
    parent_email = models.CharField(max_length=500, blank=True, null=True, default=None)
    parent_phone = models.CharField(max_length=500, blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    class Meta:
        db_table = "Athletes"

class LeagueQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Athlete, on_delete=models.SET_NULL, blank=False, null= True )
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, blank=False, null= True )
    question = models.CharField(max_length=500, blank=True, null=True, default=None)
    answer = models.CharField(max_length=500, blank=True, null=True, default=None)
    document = models.CharField(max_length=500, blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.question} {self.event}"

    class Meta:
        db_table = "League Questions"

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    division = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "Teams"   

class EventClaim(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Athlete, on_delete=models.SET_NULL, blank=False, null= True )
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, blank=False, null= True )
    status = models.CharField(max_length=100, default="draft")
    league_questions = models.ManyToManyField(LeagueQuestions)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.user} {self.event}"

    class Meta:
        db_table = "Event Claims"