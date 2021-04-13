from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    files = models.FileField(upload_to='report/media/')


    def __str__(self):
        return self.title




