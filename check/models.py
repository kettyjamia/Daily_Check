from django.db import models
from django.urls import reverse
from django.utils import timezone
# from datetime import datetime  # import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

class Satellite(models.Model):
    satellite=models.CharField(max_length=50)
    sat_id = models.IntegerField()
    def __str__(self):
        return self.satellite

class reference_input(models.Model):
    satellite = models.ForeignKey(Satellite,on_delete=models.CASCADE,related_name='reference_input')
    reason=models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='uploads/%Y/%m/%d/',null=True,blank=True)
    def __str__(self):
        return self.reason


class pids_status(models.Model):
    satellite = models.ForeignKey(Satellite,on_delete=models.CASCADE,related_name='pids_status')
    pid_number=models.PositiveIntegerField(default=1000)
    pid_status=models.CharField(max_length=50)
    mnemonic=models.CharField(max_length=50)
    reason=models.ForeignKey(reference_input,on_delete=models.CASCADE,related_name='pids_status')


    

    
