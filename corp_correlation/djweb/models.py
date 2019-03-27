from django.db import models


class Company(models.Model):
    # general class for all companies regardless of affiliation
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, default='')
    competitors = models.ManyToManyField("self", blank=True)
    has_clients = models.ManyToManyField("self", blank=True)
    client_of = models.ManyToManyField("self", blank=True)

    class Meta:
        abstract = True


class User(Company):
    # only for current clients
    pass


class Other(Company):
    # for other non-clients
    pass
