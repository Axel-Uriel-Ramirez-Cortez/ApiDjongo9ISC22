from django.db import models
from django.utils import timezone

class encuestaSatisfaccion(models.Model):
    pregunta1 = models.CharField(max_length=2)
    pregunta2 = models.TextField()
    pregunta3 = models.CharField(max_length=10)
    pregunta4 = models.TextField()
    pregunta5 = models.TextField()
    pregunta6 = models.CharField(max_length=20)
    pregunta7 = models.CharField(max_length=10)

    def str(self):
        return str(self.nombre_completo)
# Create your models here