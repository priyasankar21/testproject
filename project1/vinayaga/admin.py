from django.contrib import admin
from .models import detail,buyer
# Register your models here.
admin.site.register(buyer)
class detailAdmin(admin.ModelAdmin):
    list_display = ('Company_name', 'Company_address', 'Machine_name','Mobile_number','Image') # list of fields display in admin table
    search_fields = ('Company_name', 'Machine_name') # list of fields search in admin table
    #exclude = ('phone',)   # exclude list of fields those not display in admin form
    #sortable_by = 'first_name'  # field 'id' sorted by descending order

#admin.site.register(detail)

admin.site.register(detail, detailAdmin)