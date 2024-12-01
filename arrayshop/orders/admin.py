from django.contrib import admin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe
# Register your models here.


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


def order_stripe_payment(obj):
    url = obj.get_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank"> {obj.stripe_id}</a>'
        return mark_safe(html)
    return ''
order_stripe_payment.short_description = 'Stripe payment'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name','last_name', 'email',
                    'adress', 'postal_code','city', 'created',
                    order_stripe_payment,'updated', 'paid']
    list_filter = ['paid', 'created']
    inlines = [OrderItemInLine]