from DjangoLearn.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name