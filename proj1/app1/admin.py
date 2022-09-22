from django.contrib import admin
from .models import Customer,Product,CustomerInvoice,CustomerOrder
# Register your models here.

admin.site.register(Customer)
# admin.site.register(Vendor)
# admin.site.register(Category)
# admin.site.register(GST)
# admin.site.register(Discount)
admin.site.register(Product)
# admin.site.register(PurchaseOrder)
# admin.site.register(VendorInvoice)
admin.site.register(CustomerInvoice)
admin.site.register(CustomerOrder)
# admin.site.register(BalanceSheet)




