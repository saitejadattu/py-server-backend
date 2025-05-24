from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.email}"




class Server(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length = 100)
    description = models.TextField()
    tag = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name} - {self.ip_address}"
    
class Alert(models.Model):
    class SeverityChoices(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        CRITICAL = 'critical', 'critical'

    server = models.ForeignKey('Server', on_delete=models.CASCADE)
    severity = models.CharField(max_length=10, choices=SeverityChoices.choices)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.server} - {self.severity} - {self.message}"
class ResourceUsage(models.Model):
    server_id = models.ForeignKey(Server, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    cpu_usage_percent = models.FloatField(5.2)
    ram_usage_percent = models.FloatField(5.2)
    disk_usage_percent = models.FloatField(5.2)
    app_usage_percent = models.FloatField(5.2)
    def __str__(self):
        return f"{self.server_id} - {self.time_stamp} - {self.cpu_usage_percent} - {self.ram_usage_percent} - {self.disk_usage_percent} - {self.app_usage_percent}"

class NetworkTraffic(models.Model):
    server_id = models.ForeignKey(Server, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    incoming_traffic = models.FloatField(5.2)
