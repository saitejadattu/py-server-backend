from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('servers/', views.servers, name='servers'),
    path('server/', views.insert_server, name='insert_server'),
    path('server/<int:server_id>/', views.server, name="server"),
    path('get_user/', views.get_user, name='get_user'),
    path('server/<int:server_id>/alerts/summary/', views.server_alerts_summary, name='server_alerts_summary'),
    path('alerts/', views.alerts, name = "alerts"),
    path('server/<int:server_id>/alert/', views.alert, name='alert'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    ]