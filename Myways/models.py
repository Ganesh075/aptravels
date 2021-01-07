from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Exfd(models.Model):
	g = [('M','Male'),('FM','FeMale')]
	clg = [('AANM',"AANM & VVRSR Polytechnic - GDLR"),('SVGP',"S.V Govt Polytechnic"),('AANMR',"AANM & VVRSR Polytechnic - RJYD")]
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=10,choices=g)
	rollno = models.CharField(max_length=10)
	collegename = models.CharField(max_length=7,choices=clg)
	impf = models.ImageField(upload_to="Profile/",default="profile.jpeg") 

@receiver(post_save,sender=User)
def Crpf(sender,instance,created,**kwargs):
	if created:
		Exfd.objects.create(d=instance)

class Data(models.Model):
	busclas = [('Pallevellugu','Pallevellugu'),('Express','Express'),('Ultra Deluxe','Ultra Deluxe')]
	source = models.CharField(max_length=30)
	destination = models.CharField(max_length=30)
	busid = models.CharField(max_length=10)
	busim = models.ImageField(upload_to="Bus_Image/",null=True,default="bus.jpg")
	distance = models.CharField(max_length=10,null=True)
	cost = models.CharField(max_length=15,null=True)
	timmings = models.CharField(max_length=30)
	d = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	busclass = models.CharField(max_length=15,choices=busclas)
	da = models.DateField(null=True)

	def __str__(self):
		return self.source + self.destination
	class Meta:
		db_table = 'data'
