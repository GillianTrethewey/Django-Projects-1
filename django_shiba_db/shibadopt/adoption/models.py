from django.db import models

# Here we define our data model:
# - It consists of one type of "thing" (called a "Model")
# - This is how we will store info about our Shibas
class Shiba(models.Model):
    # CharField refers to text
    image_src = models.CharField(max_length=127)
    name = models.CharField(max_length=127)
    # IntegerField refers to a number
    age = models.IntegerField()
#Django adds an ID

