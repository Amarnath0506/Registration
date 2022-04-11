from django.db import models


# Create your models here


class Student(models.Model):
    name=models.CharField(max_length = 50, blank = True, null = True)
    email=models.EmailField(max_length = 254)
    mobile=models.CharField(max_length = 10,blank = True, null = True)
    s_class=models.CharField(max_length=50, blank=True, null=True,verbose_name='class')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}".format(self.name)