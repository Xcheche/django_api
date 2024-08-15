from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10,default=0)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")