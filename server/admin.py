__author__ = 'mpetyx'


from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Plug, Counter, Sensor, Value

class ValueAdmin(admin.ModelAdmin):
    pass

class PlugAdmin(admin.ModelAdmin):
    pass

class CounterAdmin(admin.ModelAdmin):
    pass

class SensorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Value, ValueAdmin)
admin.site.register(Plug, PlugAdmin)
admin.site.register(Counter, CounterAdmin)
admin.site.register(Sensor, SensorAdmin)