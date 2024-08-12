from django.contrib import admin
from sManager.models import Supplier, Product, Debt, Client, Money
# Register your models here.
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Debt)
admin.site.register(Money)