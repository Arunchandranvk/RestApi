from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

dishes=[
    {"id":1,"name":"carrot halwa","genere":"sweat","mainincredient":"carrot"},
    {"id":2,"name":"ChickenFry","genere":"spicy","mainincredient":"chicken"},
    {"id":3,"name":"chili chicken","genere":"spicy","mainincredient":"chicken"},
    {"id":4,"name":"icecream","genere":"cold","mainincredient":"icecream"},
]

# movies=[
#     {"id":1,"name":"sphadikham","year":1996,"director":"bhadhran","general":"drama"},
#     {"id":2,"name":"drishyam","year":2013,"director":"githu joseph","general":"drama"},
#     {"id":3,"name":"premam","year":2015,"director":"alphones","general":"romance"},
#     {"id":4,"name":"lucifer","year":2019,"director":"prithwiraj","general":"action"},
#     {"id":5,"name":"iron man","year":2008,"director":"john favru","general":"action"},
#     {"id":6,"name":"DSMM","year":2022,"director":"sam raimi","general":"fantasy"}
# ]

class Dishes(models.Model):
    name=models.CharField(max_length=100)
    genere=models.CharField(max_length=100)
    mainincredient=models.CharField(max_length=100)
    price=models.IntegerField()

class Review(models.Model):
    review=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="r_user")    
    dish=models.ForeignKey(Dishes,on_delete=models.CASCADE,related_name="r_dish")    