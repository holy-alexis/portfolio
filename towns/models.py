from django.db import models


class Town(models.Model):
    town_name = models.CharField(max_length=200)

    def __str__(self):
        return self.get_town_name()

    def get_town_name(self):
        return self.town_name


class People(models.Model):
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname
