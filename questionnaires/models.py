from django.db import models

class User(models.Model):
  first_name = models.CharField(max_length=254)
  last_name = models.CharField(max_length=254)
  email = models.EmailField(max_length=254)

class CollectedData(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField('date')