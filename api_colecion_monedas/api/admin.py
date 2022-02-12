from django.contrib import admin
from .models import Coin, Collection, Collector
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.


#-----------------------------------------------------

class MonedaResource(resources.ModelResource):
    class Meta:
        model = Coin

#-----------------------------------------------------
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'amount']


class MonedaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id', 'coin_number','id_collection','name', 'year']

class CollectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']




admin.site.register(Coin, MonedaAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Collector, CollectorAdmin)