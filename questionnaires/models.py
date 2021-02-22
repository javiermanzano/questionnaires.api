from django.db import models

class CollectedData(models.Model):
  first_name = models.CharField(max_length=254)
  last_name = models.CharField(max_length=254)
  email = models.EmailField(max_length=254)
  providers = models.CharField(max_length=254)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.providers