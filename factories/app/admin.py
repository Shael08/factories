
from django.contrib import admin
from .models import factory
from .models import customer
from .models import depot
from .models import factory_to_customer_shipping
from .models import factory_to_depots_shipping
from .models import depot_to_customer_shipping


# Register your models here.

admin.site.register(factory)
admin.site.register(customer)
admin.site.register(depot)
admin.site.register(factory_to_customer_shipping)
admin.site.register(factory_to_depots_shipping)
admin.site.register(depot_to_customer_shipping)