from django.contrib import admin
from .models import Amount, Orders

class Amount(admin.TabularInline):
    model = Amount

class OrdersAdmin(admin.ModelAdmin):
    inlines = [Amount]
    class Meta:
        model = Orders


admin.site.register(Orders, OrdersAdmin)

from django.contrib.admin.sites import AlreadyRegistered
from django.apps import apps

app_models = apps.get_app_config('app1').get_models()

for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass



