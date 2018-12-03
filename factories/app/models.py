
from django.db import models
from django.utils import timezone


class factory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    capacity = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class customer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    demand = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class depot(models.Model):
    name = models.CharField(max_length=200, unique=True)
    throughput = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class factory_to_customer_shipping(models.Model):
    factory_fk = models.ForeignKey(factory, on_delete=models.CASCADE);
    customer_fk = models.ForeignKey(customer, on_delete=models.CASCADE);
    cost = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = ('factory_fk', 'customer_fk',)

    def publish(self):
        self.save()

    def __str__(self):
        return 'Shipping from %s to %s' % (str(self.factory_fk.name), str(self.customer_fk.name))

class factory_to_depots_shipping(models.Model):
    factory_fk = models.ForeignKey(factory, on_delete=models.CASCADE);
    depot_fk = models.ForeignKey(depot, on_delete=models.CASCADE);
    cost = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = ('factory_fk', 'depot_fk',)

    def publish(self):
        self.save()

    def __str__(self):
        return 'Shipping from %s to %s' % (str(self.factory_fk.name), str(self.depot_fk.name))

class depot_to_customer_shipping(models.Model):
    depot_fk = models.ForeignKey(depot, on_delete=models.CASCADE);
    customer_fk = models.ForeignKey(customer, on_delete=models.CASCADE);
    cost = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = ('depot_fk', 'customer_fk',)

    def publish(self):
        self.save()

    def __str__(self):
        return 'Shipping from %s to %s' % (str(self.depot_fk.name), str(self.customer_fk.name))