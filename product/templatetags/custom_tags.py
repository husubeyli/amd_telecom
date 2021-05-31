from django.template import Library
from account.models import Customer
from order.models import Order
from django.shortcuts import get_object_or_404
from django.conf import settings
register = Library()
from product.models import Category


@register.simple_tag(takes_context=True)
def get_order_item_id(context, product_id):
    request = context['request']

    device = request.COOKIES.get('device')
    customer, created = Customer.objects.get_or_create(device=device)

    try:
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print('order id:', order.id)
        print('product id', product_id)
    except Order.DoesNotExist:
        order = None

    if order != None:
        # try:
            # orderItems_id = order.orderitem_set.all().get(product_id=product_id).id
        orderItems_id = order.orderitem_set.all().filter(product_id=product_id).first()
        # except order.orderitem_set.all().get(product_id=product_id).DoesNotExist:
            # orderItems_id = None
        print('ordetItems_id', orderItems_id)
        return orderItems_id
    else:
        return None


@register.simple_tag
def get_navbar():
    category_list = Category.objects.order_by('created_at')
    
    # last_s_index = len(meny_list_main) - 2
    context = {
        'api_url': settings.API_URL,
        'category_list': category_list,
        # 'last_second_index': last_s_index
    }
    return context


# @register.filter
# def index(indexable, i):

#     return value
