from django.db import models

# Create your models here.
class Cupon(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=5)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Cupones"

class BlackListedCupon(models.Model):
    id = models.AutoField(primary_key=True)
    cupon_id = models.ForeignKey(Cupon, on_delete=models.CASCADE)

