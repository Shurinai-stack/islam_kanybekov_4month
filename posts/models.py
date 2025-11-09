from django.db import models

# Create your models here.

class Categorys(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000, null=True, blank=True)
    rate = models.IntegerField(default=0)
    category = models.ForeignKey(Categorys, null=True, blank=True, on_delete=models.CASCADE)  
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.title} - {self.content} - {self.rate}"