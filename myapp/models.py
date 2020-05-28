from django.db import models

# Create your models here.


# create category fields models

class Category(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title

# create a image   modes for image

class Images(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')
    timestamp = models.DateField()
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title