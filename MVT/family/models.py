from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dni = models.IntegerField()
    age = models.DateField()

    def __str__(self):
        return f"{self.name} {self.last_name} - DNI: {self.dni} - Fecha nacimiento:{self.age}"
