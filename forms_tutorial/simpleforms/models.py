from django.db import models


class GetAnimal(models.Model):
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    name = models.CharField(max_length=100, blank=True, null=True)


class Organization(models.Model):
    organization = models.CharField(max_length=50)

    def __str__(self):
        return self.organization


class Executive(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.title})"


class Manager(models.Model):
    boss = models.ForeignKey(Executive, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.title})"


class Employee(models.Model):
    boss = models.ForeignKey(Manager, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.title})"
