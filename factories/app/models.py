
from django.db import models
from django.utils import timezone


class factory(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class costumer(models.Model):
    name = models.CharField(max_length=200)
    demand = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class depot(models.Model):
    name = models.CharField(max_length=200)
    troughput = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class factory_to_costumer_shipping(models.Model):
    factory_fk = models.ForeignKey(factory , on_delete=models.CASCADE);
    costumer_fk = models.ForeignKey(costumer , on_delete=models.CASCADE);
    cost = models.FloatField()
    quantity = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return "nem tudom mivel terjek vissza"

class factory_to_depots_shipping(models.Model):
    factory_fk = models.ForeignKey(factory , on_delete=models.CASCADE);
    depot_fk = models.ForeignKey(depot, on_delete=models.CASCADE);
    cost = models.FloatField()
    quantity = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return "nem tudom mivel terjek vissza"

class depot_to_costumer_shipping(models.Model):
    depot_fk = models.ForeignKey(depot , on_delete=models.CASCADE);
    costumer_fk = models.ForeignKey(costumer , on_delete=models.CASCADE);
    cost = models.FloatField()
    quantity = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return "nem tudom mivel terjek vissza"