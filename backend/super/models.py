from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.




class Video(models.Model):
    choice = ( 
    ("1", "COMEDY"), 
    ("2", "ACTION"), 
    ("3", "ROMANTIC"), 
    ("4", "HORROR"), 
    ("5", "SCIENCE FICTION"), 
    
)   
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=choice, default=1, verbose_name='category')
    description = models.TextField(blank=True)
    trending = models.BooleanField(default=False)
    videoFile = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Subscription_Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    id = models.AutoField(primary_key=True)
    planname = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    plan_price = models.DecimalField(max_digits=5, decimal_places=2)
    validity = models.PositiveIntegerField()
    planAdded = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.planname
    
