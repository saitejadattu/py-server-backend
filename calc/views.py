from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User,Server,Alert,ResourceUsage,NetworkTraffic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def home(request):
    return render(request,'home.html')
    # return HttpResponse("<h1>Calculator Home</h1>")

def add(request):
    if(request.method == 'POST'):
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        result = int(num1) + int(num2)
        return render(request,'result.html', {'result': result})
    
def get_user(request):
    if(request.method == 'GET'):
        users = list(User.objects.all().values())
        return JsonResponse(users, safe=False)

@api_view(['GET'])
def servers(request):
    if(request.method == "GET"):
        servers = Server.objects.values()
        return Response(servers, status=status.HTTP_200_OK)
@api_view(['PUT','DELETE', 'GET'])
def server(request, server_id):
    if(request.method == "GET"):
        try:
            server = Server.objects.get(id=server_id)
            server = {
                "name": server.name,
                "ip_address": server.ip_address,
                "location": server.location,
                "description": server.description,
                "is_active": server.is_active,
                "tag":server.tag
            }
            return Response(server, status= status.HTTP_200_OK)
        except:
            return Response("Server not found", status=status.HTTP_404_NOT_FOUND)    
    if(request.method == "DELETE"):
        try:
            server = Server.objects.get(id=server_id)
            server.delete()
            return Response('server deleted', status=status.HTTP_200_OK)
        except:
            return Response("Server not found", status=status.HTTP_404_NOT_FOUND)
    if(request.method == "PUT"):
        data = request.data
        try:
            server = Server.objects.get(id=server_id)
            server.name = data["name"]
            server.ip_address = data["ip_address"]
            server.location = data["location"]
            server.description = data["description"]
            server.is_active = data["is_active"]
            server.tag = data["tag"]
            server.save()
            print(data)
            print(server.location)
           
            return Response("Server is Updated", status=status.HTTP_201_CREATED)
        except:
            return Response("Server not Found", status=status.HTTP_404_NOT_FOUND)
    if(request.method == "POST"):
        try:
            server = Server.objects.get(id=server_id)
            print(server)
            return Response("Server is created", status=status.HTTP_201_CREATED)
        except:
            return Response("Server Not Found",status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def insert_server(request):
    if(request.method == "POST"):
        try:
            server = Server(
                name=request.data['name'],
                ip_address=request.data['ip_address'],
                location=request.data['location'],
                description=request.data['description'],
                tag=request.data['tag'],
                is_active=request.data['is_active'],
                )
            server.save()
            return Response("Server is created", status=status.HTTP_201_CREATED)
        except:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
@api_view(['GET','PUT','DELETE'])
def server_alerts_summary(request, server_id):
    if(request.method == "GET"):
        try:
            server = Server.objects.get(id=server_id)
            alerts = server.alert_set.all()
            return Response(alerts.values(), status=status.HTTP_200_OK)
        except:
            return Response("Server not found", status=status.HTTP_404_NOT_FOUND)
    if(request.method == "PUT"):
        try:
            server = Server.objects.get(id=server_id)
            alert = Alert.objects(server= server, severity=request.data['severity'], message=request.data['message'])
            alert.save()
            return Response("Server is updated", status=status.HTTP_200_OK)
        except:
            return Response("Server not found", status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST', "DELETE", "GET", "PUT"])
def alert(request, server_id):
    if(request.method == "POST"):
        try:
            server = Server.objects.get(id=request.data['server'])
            alert = Alert(
                server=server,
                severity=request.data['severity'],
                message=request.data['message'],
            )
            alert.save()
            return Response("Alert is created", status=status.HTTP_201_CREATED)
        except:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
    if(request.method == "PUT"):
        try:
            server = Server.objects.get(id=server_id)
            
        except:
            return Response("Alert is updated", status=status.HTTP_404_NOT_FOUND)
        
@api_view(["GET","POST"])
def alerts(request):
    if(request.method == "GET"):
        alerts = Alert.objects.values()
        return Response(alerts, status=status.HTTP_200_OK)
    

class LoginView(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email
        })