from distutils.command.upload import upload
from django.db import models



class Food(models.Model):
    FOOD_TYPE = [
        ("breakfast", "Breakfast"),
        ("drinks", "Drink"),
        ("dinner", "Dinner"),
        ("lunch", "Lunch")
    ]

    name = models.CharField(max_length=60)
    description = models.TextField()
    rate = models.IntegerField()
    price = models.IntegerField()
    time = models.IntegerField()
    pub_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/foods/')
    type_food = models.CharField(max_length=10, choices=FOOD_TYPE, default="drinks")


    def __str__(self):
        return self.name


class Stuff(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/staff')
    job = models.CharField(max_length=150)
    about = models.TextField()

    def __str__(self):
        return self.name