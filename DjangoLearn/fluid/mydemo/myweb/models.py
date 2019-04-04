from django.db import models

# Create your models here.
class Fluid(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = "fluid"
