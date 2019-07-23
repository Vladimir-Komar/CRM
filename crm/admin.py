from django.contrib import admin
from .models import Customer, Provider, Product, Deal


admin.site.register(Customer)
admin.site.register(Provider)
admin.site.register(Product)
# admin.site.register(Deal)


# @admin.register(Deal)
# class DealAdmin(admin.ModelAdmin):
#
#     list_display = ["customer","product","deal_price"]
#
#     list_display_links = ["customer","deal_date"]
#
#     search_fields = ["customer"]
#
#     list_filter = ["deal_date"]
#
#     class Meta:
#         model = Deal
