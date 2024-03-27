from django.db import models



class Book(models.Model):
    Title = models.CharField(max_length=32,null=False,blank=False)
    Author = models.CharField(max_length=32,null=False,blank=False)
    Publication_Date = models.DateField(null=True,blank=True)
    ISBN = models.CharField(max_length=13,unique=True)
    Description = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.Title
