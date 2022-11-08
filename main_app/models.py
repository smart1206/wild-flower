from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Use(models.Model):
    name = models.CharField(max_length=50)
    use = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}{self.use}'

    def get_absolute_url(self):
        return reverse('uses_detail',
        kwargs={'pk': self.id})


class Flower(models.Model):
    name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    petals = models.IntegerField()
    size = models.IntegerField('Size in Inches')
    leaf_arrangement = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    uses = models.ManyToManyField(Use)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'flower_id': self.id})

class Sighting(models.Model):
    date = models.DateField('Sighting Date')
    # maybe later add habitat options
    location = models.CharField(max_length=75)

    flower =models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__(self):
        return f"Spotted at {self.location} on {self.date}"