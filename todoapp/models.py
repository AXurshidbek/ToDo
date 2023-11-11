from django.db import models
from django.contrib.auth.models import User


HOLAT=(
    ('Bajarilyapti', 'Bajarilyapti'),
    ('Bajarilmadi', 'Bajarilmadi'),
    ('Tugallandi', 'Tugallandi')
)
class Reja(models.Model):
    sarlavha=models.CharField(max_length=55)
    batafsil=models.TextField()
    sana=models.DateField()
    holati=models.CharField(max_length=25, choices=HOLAT)
    egasi=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.sarlavha