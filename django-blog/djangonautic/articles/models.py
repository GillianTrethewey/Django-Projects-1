from django.db import models

# Create your models here.
from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField() # default widget is TextArea
    date=models.DateTimeField(auto_now_add=True) #cap in python
    # add in thumbnail later
    # add in author later

    def __str__(self): 
        return self.title