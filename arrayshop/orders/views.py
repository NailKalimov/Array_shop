from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreatedForm
from cart.cart import Cart
from .tasks import order_created
from django.urls import reverse

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreatedForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
                cart.clear()
                order_created.delay(order.id)
                request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreatedForm()
    return render(request,
                  template_name='orders/order/create.html',
                  context={'cart': cart, 'form': form})
    