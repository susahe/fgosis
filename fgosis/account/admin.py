from django.contrib import admin
from account.models import Payment 


# Add in this class to customized the Admin Interface
class PaymentAdmin(admin.ModelAdmin):
	list_display = ('name', )
	


admin.site.register(Payment, PaymentAdmin)

