from __future__ import unicode_literals
from django.contrib.auth.models import User
from stockapp.models import info
from django.db import models

# Create your models here.
#from stockapp.models import info

class Fav(models.Model):
	username = models.ForeignKey(User)
	stock = models.CharField(max_length= 6,default="")





# class fav(models.Model):
# 	#st= info()
# 	stocksymbol= models.ForeignKey(user, max_length=6)
	#user= models.ForeignKey(User)

