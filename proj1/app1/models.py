from django.db import models
from django.db.models import CASCADE

# # Create your models here.
# class Customer(models.Model):
#     c_id = models.AutoField(primary_key=True)
#     c_name = models.CharField(max_length=100, null=True, blank=True)
#     c_email = models.EmailField(unique=True)
#     c_phone = models.IntegerField(unique=True)
#     c_address = models.CharField(max_length=255, null=True, blank=True)
#     def __str__(self):
#         return f"{self.c_name}"

# class Vendor(models.Model):
#     v_id = models.AutoField(primary_key=True)
#     v_name = models.CharField(max_length=100)
#     v_phone = models.IntegerField(unique=True)
#     v_email = models.EmailField(unique=True)
#     v_address = models.CharField(max_length=255, null=True, blank=True)
#     v_gst_no = models.CharField(max_length=50)
#     def __str__(self):
#         return f"{self.v_id}---{self.v_name}---{self.v_phone}---{self.v_email}---{self.v_address}---{self.v_gst_no}"


# class Category(models.Model):
#     cat_id = models.AutoField(primary_key=True)
#     cat_name = models.CharField(max_length=100)
#     cat_desc = models.CharField(max_length=255)
#     def __str__(self):
#         return f"{self.cat_name}"

# class GST(models.Model):
#     gst_id = models.AutoField(primary_key=True)
#     category = models.ForeignKey(Category, on_delete=CASCADE)
#     igst = models.IntegerField()
#     hsn_code = models.IntegerField(unique=True)
#     def __str__(self):
#         return f"{self.category}---{self.hsn_code}"


# class Discount(models.Model):
#     discount_id = models.IntegerField(primary_key=True)
#     product_name = models.CharField(max_length=100)
#     desc = models.CharField(max_length=255)
#     discount = models.FloatField()
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     def __str__(self):
#         return f"{self.product_name}---{self.discount}"


# class Product(models.Model):
#     p_id = models.AutoField(primary_key=True)
#     p_name = models.CharField(max_length=100)
#     p_img = models.ImageField(upload_to='product')
#     category = models.ForeignKey(Category, on_delete=CASCADE)
#     p_price = models.FloatField()
#     vendor = models.ForeignKey(Vendor, on_delete=CASCADE)
#     product_stock = models.FloatField()
#     unit = models.CharField(max_length=100)
#     reorder_level = models.FloatField()
#     discount = models.ForeignKey(Discount, on_delete=CASCADE)
#     gst = models.ForeignKey(GST, on_delete=CASCADE)
#     def __str__(self):
#         return f"{self.p_name}"

# class 	
#     vendor = models.ForeignKey(Vendor, on_delete=CASCADE)
#     product = models.ForeignKey(Product, on_delete=CASCADE)
#     total_amount = models.FloatField(default=200000)
#     def __str__(self):
#         return f"Purches Order:{self.po_id}--- Product:{self.product}"


# class VendorInvoice(models.Model):
#     v_invoice_id = models.AutoField(primary_key=True)
#     vendor = models.ForeignKey(Vendor, on_delete=CASCADE)
#     purchaseorder = models.ForeignKey(PurchaseOrder, on_delete=CASCADE, default=True)
#     # total_amount = models.ForeignKey(PurchaseOrder, on_delete=CASCADE, default=True)
#     date = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"{self.v_invoice_id}---{self.vendor}---{self.date}"

# payment = (('cash','Cash'),('Online','Online'))
# class CustomerInvoice(models.Model):
#     invoice_id = models.AutoField(primary_key=True)
#     customer = models.ForeignKey(Customer,on_delete=CASCADE)
#     gross_cost = models.FloatField(default=0)
#     tax_amount  = models.FloatField(default=0)
#     discount = models.ForeignKey(Discount, on_delete=CASCADE)
#     net_amount = models.FloatField(default=0)
#     payment_mode = models.CharField(choices=payment, max_length=50)
#     transaction_id = models.IntegerField(null=True, blank=True)
#     invoice_date = models.DateTimeField()
#     total_amount = models.IntegerField()
#     def __str__(self):
#         return f"{self.customer}"



# class CustomerOrder(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     # customerinvoice = models.ForeignKey(CustomerInvoice, on_delete=CASCADE)
#     product = models.ForeignKey(Product, on_delete=CASCADE)
#     quantity = models.PositiveIntegerField()
#     def __str__(self):
#         return f"{self.order_id}---{self.product}---{self.quantity}"


# payment = (('cash', 'Cash'), ('Online', 'Online'))
# class CustomerInvoice(models.Model):
#     invoice_id = models.AutoField(primary_key=True)
#     product = models.ForeignKey(Product, on_delete=CASCADE, default=True)
#     customer = models.ForeignKey(CustomerOrder, on_delete=CASCADE)
#     gross_cost = models.FloatField(default=0)
#     tax_amount = models.FloatField(default=0)
#     discount = models.ForeignKey(Discount, on_delete=CASCADE)
#     net_amount = models.FloatField(default=0)
#     payment_mode = models.CharField(choices=payment, max_length=50)
#     transaction_id = models.IntegerField(null=True, blank=True)
#     invoice_date = models.DateTimeField()
#     total_amount = models.IntegerField()
#     def __str__(self):
#         return f"{self.customer}"

# class BalanceSheet(models.Model):
#     bs_id = models.AutoField(primary_key=True)
#     vendorinvoice = models.ForeignKey(VendorInvoice, on_delete=CASCADE)
#     customerinvoice = models.ForeignKey(CustomerInvoice, on_delete=CASCADE)
#     light_bill = models.FloatField()
#     emp_salary = models.FloatField()
#     monthly_rent = models.FloatField()
#     miscellaneous = models.FloatField()
#     bs_date = models.DateField()
#     def __str__(self):
#         return f"{self.bs_id}"


class Product(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=100)
    #p_img = models.ImageField(upload_to='product')
    #category = models.ForeignKey(Category, on_delete=CASCADE)
    p_price = models.FloatField()
    #vendor = models.ForeignKey(Vendor, on_delete=CASCADE)
    product_stock = models.FloatField()
    unit = models.CharField(max_length=100)
    reorder_level = models.FloatField()
    #discount = models.ForeignKey(Discount, on_delete=CASCADE)
    #gst = models.ForeignKey(GST, on_delete=CASCADE)
    def __str__(self):
        return f"{self.p_name}"

class Customer(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_name = models.CharField(max_length=100, null=True, blank=True)
    c_email = models.EmailField(unique=True)
    #c_phone = models.IntegerField(unique=True)
    #c_address = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"{self.c_name}"

class CustomerOrder(models.Model):
    order_id = models.IntegerField(primary_key=True)
    # customerinvoice = models.ForeignKey(CustomerInvoice, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.order_id}---{self.product}---{self.quantity}"


payment = (('cash', 'Cash'), ('Online', 'Online'))
class CustomerInvoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=CASCADE, default=True)
    customer = models.ForeignKey(CustomerOrder, on_delete=CASCADE)
    gross_cost = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    #discount = models.ForeignKey(Discount, on_delete=CASCADE)
    net_amount = models.FloatField(default=0)
    payment_mode = models.CharField(choices=payment, max_length=50)
    transaction_id = models.IntegerField(null=True, blank=True)
    invoice_date = models.DateTimeField()
    total_amount = models.IntegerField()
    def __str__(self):
        return f"{self.customer}"



