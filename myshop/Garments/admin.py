from django.contrib import admin
from Garments.models import Formalshirt,Trousers
class FormalShirtAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'created', 'updated')
class TrousersAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'created', 'updated')
# Register your models here.
admin.site.register(Trousers,TrousersAdmin)
admin.site.register(Formalshirt, FormalShirtAdmin)



