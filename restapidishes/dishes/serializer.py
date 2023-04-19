from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class DishSerializer(serializers.Serializer):
    name=serializers.CharField()
    genere=serializers.CharField()
    mainincredient=serializers.CharField()
    price=serializers.CharField()

class DishModelser(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        fields="__all__"


class UserSer(serializers.ModelSerializer):
    class Meta:
        model=User      
        fields=["username","password","email"] 
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)     


class DishReviewSer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['review','rating']
    def create(self,validated_data):
        user=self.context.get("user")
        mv=self.context.get("movie")
        return Review.objects.create(**validated_data,user=user,di=mv)



