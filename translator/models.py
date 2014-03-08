from django.db import models

# Create your models here.
class Good(models.Model):
    def __unicode__(self):
        return self.text
    text = models.CharField(max_length = 256)
    
class Bad(models.Model):
    def __unicode__(self):
        return self.text
    text = models.CharField(max_length = 256)
    category = models.CharField(max_length = 64)
    maps = models.ForeignKey(Good)