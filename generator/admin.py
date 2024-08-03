from django.contrib import admin
from .models import Invoice, Receipt


from solo.admin import SingletonModelAdmin
from .models import PaymentInformation


class ReceiptInline(admin.StackedInline):
    model = Receipt
    extra = 0
    max_num = 1
    can_delete = False
    
    readonly_fields = ('created',)
    
    



@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    
    search_fields = ('invoice_number', )
    ordering = ('-created',)
    date_hierarchy = 'created'
    inlines = [ReceiptInline]  

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    ordering = ('-created',)
    



admin.site.register(PaymentInformation, SingletonModelAdmin)
