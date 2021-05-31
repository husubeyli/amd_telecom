from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls.base import reverse_lazy
from django.contrib.messages import success, error
# Create your views here.

from account.models import Customer

from .models import OrderItem, Order
from .forms import CheckoutForm
from .signals import send_form



# def deletefromcart(request, id):
#     cartitem = OrderItem.objects.get(id=id)
#     cartitem.delete()
#     return redirect('cart')


def cart(request):
    show_order_items = None
    # device = request.COOKIES['device']
    device = request.COOKIES.get('device')
    customer, created = Customer.objects.get_or_create(device=device)
    print('customer', customer)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    print('order', order)
    items = order.orderitem_set.all()
    print('items:', order.orderitem_set.all())
    imgs = {}
    print("orderin folsudumu", order.complete)
    if not order.complete:
        show_order_items = True

        for item in items:
            print('cart-item:', item)
            print('cart-item.product:', item.product)
            imgs.update({item.id: item.product.images.get(is_main=True).imageURL})  
        print('order', order)
        print('imgs', imgs)
        print('orderitemler:', order.orderitem_set.all())
    else:
        order = None
    print("order: bu", show_order_items)
    # print("Carta girende imgs: ", imgs[item.id].first())
    context = { 'show_order_items': show_order_items, 'order':order, 'imgs': imgs}
    return render(request, 'cart.html', context)

def checkout(request):
    device = request.COOKIES.get('device')

    customer, created = Customer.objects.get_or_create(device=device)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    items = order.orderitem_set.all()
    total=0
    for item in items:
        total += item.get_total
    context = {'items': items, 'form': CheckoutForm, 'total':total, 'order': order}

    # {{order.get_discount_total|floatformat:2}}

    if request.method == 'POST':

        form = CheckoutForm(request.POST, instance=order)
        if form.is_valid():
            form.save(commit=False)
            order.complete = True
            form.save()
            send_form(instance=order)
            success(request, 'Sifarisiniz qeydə alınmışdır gün ərzində sizinlə əlaqə saxlanılılacaq.')
            return redirect('index:home')
    return render(request, 'checkout.html', context)
    




