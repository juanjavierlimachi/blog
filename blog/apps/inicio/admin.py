from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(Perfiles)
admin.site.register(Alumnos)
admin.site.register(Directores)
admin.site.register(Producto)