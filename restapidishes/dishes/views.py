from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import status,permissions,authentication
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
# Create your views here.

# class DishesList(APIView):
#     def get(self,request,*args,**kwargs):
#         if 'genere' in request.query_params:
#             qp=request.query_params.get('genere')
#             dish=[i for i in dishes if i['genere']==qp].pop()
#             return Response(data=dish)
#         if 'mainincredient' in request.query_params:
#             qp=request.query_params.get('mainincredient')
#             dish=[i for i in dishes if i['mainincredient']==qp].pop()
#             return Response(data=dish)
#         return Response(data=dishes)
    
#     def post(self,request,*args,**kwargs):
#         data=request.data
#         dishes.append(data)
#         return Response(data=dishes)

# class DishesItem(APIView):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("did")
#         dish=[i for i in dishes if i["id"]==id].pop()
#         return Response(data=dish)     
#     def put(self,request,*args,**kwargs):
#          id=kwargs.get("did")
#          data=request.data
#          dish=[i for i in dishes if i["id"]==id].pop()
#          dish.update(data)
#          return Response(data=dishes) 
#     def delete(self,request,*args,**kwargs):
#         id=kwargs.get("did")
#         dish=[i for i in dishes if i["id"]==id].pop()
#         dishes.remove(dish)
#         return Response(data=dishes)


class DishesList(APIView):
    def get(self,request,*args,**kwargs):
        dish=Dishes.objects.all()
        ser=DishSerializer(dish,many=True)
        return Response(data=ser.data)
    def post(self,request,*args,**kwargs):
        dish=request.data
        ser=DishSerializer(data=dish)
        if ser.is_valid():
            name=ser.validated_data.get("name")
            genere=ser.validated_data.get("genere")
            mi=ser.validated_data.get("mainincredient")
            price=ser.validated_data.get("price")
            Dishes.objects.create(name=name,genere=genere,mainincredient=mi,price=price)
            return Response({"msg":"ok"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)

class DishesItem(APIView):
    def get(self,request,*args,**kwargs):   
        id=kwargs.get("did")
        dish=Dishes.objects.get(id=id)
        ser=DishSerializer(dish)
        return Response(ser.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("did")
        dish=Dishes.objects.get(id=id)
        dishdata=request.data
        ser=DishSerializer(data=dishdata)
        if ser.is_valid():
            dish.name=ser.validated_data.get("name")
            dish.genere=ser.validated_data.get("genere")
            dish.mi=ser.validated_data.get("mainincredient")
            dish.price=ser.validated_data.get("price")
            dish.save()
            return Response({"msg":"Updated"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("did")
        dish=Dishes.objects.get(id=id)
        dish.delete()
        return Response({"msg":"Deleted"})
       
        
class DishMList(APIView):
    def get(self,request,*args,**kwargs):
        dhs=Dishes.objects.all()
        dser=DishModelser(dhs,many=True)
        return Response(data=dser.data)
    def post(self,request,*args,**kwargs):
        dhs=request.data
        ser=DishModelser(data=dhs)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"updated"})
        else: 
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)

class DishMItem(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("did")
        try:
            dh=Dishes.objects.get(id=id)
            dser=DishModelser(dh)
            return Response(data=dser.data)
        except:
            return Response({"msg":"invalid ID"},status=status.HTTP_400_BAD_REQUEST)
    def  delete(self,request,*args,**kwargs):
        id=kwargs.get("did")
        try:
            dh=Dishes.objects.get(id=id)
            dh.delete()
            return Response({"msg":"ok"})
        except:
            return Response({"msg":"Invalid ID"},status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,*args,**kwargs):
        try:
            id=kwargs.get("did")
            dh=Dishes.objects.get(id=id)
            ser=DishModelser(data=request.data,instance=dh)
            if ser.is_valid():
                ser.save()
                return Response({"msg":"updated"})
            else:
                return Response({"msg":ser.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"msg":"invalid ID"},status=status.HTTP_400_BAD_REQUEST)    
            
class UsercreationView(APIView):
    def post(self,request,*args,**kwargs):
        ser=UserSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Registraion Completed"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        

class DishApi(ViewSet):
    def list(self,request,*args,**kwargs):
        dv=Dishes.objects.all()
        dser=DishModelser(dv,many=True)
        return Response(data=dser.data)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            dh=Dishes.objects.get(id=id)
            dser=DishModelser(dh)
            return Response(data=dser.data)
        except:
            return Response({"msg":"invalid ID"},status=status.HTTP_400_BAD_REQUEST)
    def create(self,request,*args,**kwargs):
        ser=DishModelser(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"updated"})
        else: 
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)
    def update(self,request,*args,**kwargs):
        try:
            id=kwargs.get("pk")
            dh=Dishes.objects.get(id=id)
            ser=DishModelser(data=request.data,instance=dh)
            if ser.is_valid():
                ser.save()
                return Response({"msg":"updated"})
            else:
                return Response({"msg":ser.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"msg":"invalid ID"},status=status.HTTP_400_BAD_REQUEST)  
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("did")
        try:
            dh=Dishes.objects.filter(id=id).delete()
            return Response({"msg":"ok"})
        except:
            return Response({"msg":"Invalid ID"},status=status.HTTP_400_BAD_REQUEST)
          
               
#using modelviewset
class DishApiDV(ModelViewSet):
    serializer_class=DishModelser
    queryset=Dishes.objects.all()
    model=Dishes
    permission_classes=[permissions.IsAuthenticated]
    # authentication_classes=[authentication.TokenAuthentication]

    @action(detail=True,methods=["post"])
    def add_reviews(self,req,*args,**kwargs):
        id =kwargs.get("pk")
        mv=Dishes.objects.get(id=id)
        user=req.user
        ser=DishReviewSer(data=req.data,context={"user":user,"dish":mv})
        if ser.is_valid():
            ser.save()
            return Response ({"msg":"Added"})
        else:
            return Response({"MSG":ser.errors},status=status.HTTP_100_CONTINUE)



