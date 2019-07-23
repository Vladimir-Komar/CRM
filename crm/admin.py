from django.contrib import admin
from .models import Customer, Provider, Product, Deal


admin.site.register(Customer)
admin.site.register(Provider)
admin.site.register(Product)
# admin.site.register(Deal)


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):

    list_display = ["deal_date", "customer","product","deal_price", "profit"]

    list_display_links = ["customer","deal_date"]

    search_fields = ["deal_date"]

    list_filter = ["deal_date"]

    class Meta:
        model = Deal
