from django.contrib import admin
from .models import Chicken, Laying, Snack

# Register your models here.
admin.site.register(Chicken)
admin.site.register(Laying)
admin.site.register(Snack)