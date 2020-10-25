from django.db import models


class Verification(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    email = models.EmailField(max_length=100)
    HCN = models.CharField(max_length=100)
    Version_code=models.CharField(max_length=2)
    DOB = models.DateField((auto_now=True)
    Gender = models.CharField(max_length=5,choices=GENDER, default='Male')
    Postcal_code = models.CharField(max_length=7)
    DIN = models.CharField(max_length=11)
    connection_id = models.UUIDField()
    invite_url = models.URLField(max_length=2000)


class SessionState(models.Model):
    connection_id = models.UUIDField()
    state = models.TextField()


