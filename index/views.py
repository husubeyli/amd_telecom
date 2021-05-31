from product.models import Product
from .models import Banner
from order.models import Order
from account.models import Customer
from product.models import Product_details, Category
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


# class HomePageTemplateView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         products = Product.objects.all()
#         category = Category.objects.all()
#         details = Product_details.objects.all()

#         # for home page return filter products
#         new_arrivals = products.filter(is_published=True).filter(is_new=True).order_by('-created_at')[:12]
#         most_sold = products.filter(is_published=True).order_by('-sale_count')[:12]
#         discounted_products = products.filter(is_published=True).filter(is_discount=True).order_by('-created_at')[:12]

#         context['new_arrivals'] = new_arrivals
#         context['most_sold'] = most_sold
#         context['discounted_products'] = discounted_products
#         context["products"] = products
#         context["details"] = details
#         context["category"] = category
#         return context
    
def home_page(request):
    device = request.COOKIES.get('device')
    customer, created = Customer.objects.get_or_create(device=device)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    products = Product.objects.all()
    category = Category.objects.all()
    details = Product_details.objects.all()
    banner_main = Banner.objects.get(is_main=True)
    banner_second_yuxari = Banner.objects.get(is_second_yuxari=True)
    banner_second_ashagi = Banner.objects.get(is_second_ashagi=True)
    banner_third_sol = get_object_or_404(Banner, is_third_sol=True)
    # banner_third_sol = Banner.objects.get(is_third_sol=True)
    banner_third_sag = get_object_or_404(Banner, is_third_sag=True)
    # banner_third_sag = Banner.objects.get(is_third_sag=True)
    banner_third_orta = get_object_or_404(Banner, is_third_orta=True)
    # banner_third_orta = Banner.objects.get(is_third_orta=True)
    # for home page return filter products
    new_arrivals = products.filter(is_published=True).filter(is_new=True).order_by('-created_at')[:12]
    most_sold = products.filter(is_published=True).order_by('-sale_count')[:12]
    discounted_products = products.filter(is_published=True).filter(is_discount=True).order_by('-created_at')[:12]

    print("Main banner image", banner_main.image)

    context = {
        'products': products, 
        'details': details,
        'category': category, 
        'customer': customer, 
        'order': order, 
        'new_arrivals': new_arrivals, 
        'discounted_products': discounted_products, 
        'most_sold': most_sold,
        'banner_main': banner_main,
        'banner_second_yuxari': banner_second_yuxari,
        'banner_second_ashagi': banner_second_ashagi,
        'banner_third_sol': banner_third_sol,
        'banner_third_sag':banner_third_sag,
        'banner_third_orta': banner_third_orta
    }
    
    return render(request, 'home.html', context)


def autocomplete(request):
    print(request.GET.get("term"))
    if 'term' in request.GET:
        qs = Product.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.title)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    return render(request, 'core/home.html')