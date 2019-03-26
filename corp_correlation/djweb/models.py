from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    competitors = models.ManyToManyField("self")
    allied = models.ManyToManyField("self")

    class Meta:
        abstract = True


class Client(Company):
    pass


class Competitor(Company):
    pass
