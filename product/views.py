from datetime import datetime
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.db.models import Q
from order.models import Order
from account.models import Customer
from collections import OrderedDict
# Create your views here.
from django.http import HttpResponse
from .models import (
    Product, 
    Product_images, 
    Product_details, 
    Category,
    Marka,
)
from order.models import (
    OrderItem, 
    Order,
)
from account.models import Customer


class SearchProductListView(ListView):
    model = Product
    template_name = 'search.html'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        products = self.get_queryset
        device = self.request.COOKIES.get('device')
        customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        context = { 'products': self.get_queryset,
                    'customer': customer,
                    'order': order,}
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(is_published=True).filter(operator_code__isnull=False).order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            print(query, 'basliq')
            product = Product.objects.filter(operator_code=None).filter( Q(title__icontains=query) | Q(category__title__icontains=query)).order_by('-created_at').distinct()

        return product


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # product = get_object_or_404(Product, id=self.kwargs['pk'])
        product = Product.objects.get(slug=self.object.slug)
        the_category = Category.objects.filter(categories=product).values_list('id', flat=True).last()
        print(the_category, 'kataloq')
        related_products = Product.objects.filter(category__id=the_category).exclude(id=product.id)
        photos = Product_images.objects.filter(product=product).order_by('-is_main')
        details = Product_details.objects.filter(product=product)
        site_url = settings.API_URL
        context['product'] = product
        context['photos'] = photos
        context['details'] = details
        context['related_products'] = related_products
        context['site'] = site_url
        print(details, 'sekilci')
        return context

    def post(self, request, **kwargs):
        slug = self.kwargs['slug']
        product = Product.objects.get(slug=slug)
        #Get user account information
        try:
            customer = self.request.user.customer

        except:
            # device = self.request.COOKIES['device']
            device = self.request.COOKIES.get('device')
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(customer=customer, product=product, order=order)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()

        return redirect('order:cart')


# def product_detail(request, slug):
#     product = Product.objects.get(slug=slug)
#     photos = Product_images.objects.filter(product=product)
#     details = Product_details.objects.filter(product=product)
#     context = {'product':product,'photos':photos,'details':details}

#     if request.method == 'POST':
#         product = Product.objects.get(slug=slug)
#         #Get user account information
#         try:
#             customer = request.user.customer	
#         except:
#             device = request.COOKIES['device']
#             customer, created = Customer.objects.get_or_create(device=device)

#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
#         orderItem.quantity=request.POST['quantity']
#         orderItem.save()

#         return redirect('order:cart')

#     return render(request, 'product_detail.html', context)

    




class ProductsListView(ListView):
    model = Product
    template_name = 'products.html'
    # paginate_by = 5



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        products = Product.objects.filter(category=category).filter(is_published=True).filter()

        device = self.request.COOKIES.get('device')
        customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        # for filter 
        markas = Marka.objects.filter(marka__id__in=products.all()).filter(marka__isnull=False).distinct()

        all_l = products.exclude(color_title__isnull=True).exclude(color_title__exact='')
        colors_list = products.values('color_title')
        operators_list = products.values('operator_code')
        internal_storages_list = products.values('internal_storage')

        # for remove duplicate color title in colors_list
        colors = []
        for i in colors_list:
            if i['color_title'] != None:
                colors.append(i['color_title'])
        colors = list(dict.fromkeys(colors))

        # remove duplicate operator code in list
        operators_codes = []
        [operators_codes.append(i['operator_code']) for i in operators_list if i['operator_code'] not in operators_codes]
        print(operators_codes, 'kodlar')

        # for append list only defaul not none ram field no duplicate
        internal_storages = []
        for i in internal_storages_list:
            if i['internal_storage'] != None:
                internal_storages.append(i['internal_storage'])
        internal_storages = list(dict.fromkeys(internal_storages))
        internal_storages.sort()

        print(internal_storages, 'yaddas')

        # for filter template page for view or no
        marka = False
        color_title = False
        internal_storage = False
        condition = False
        operator = False
        operator_data = ''

        # for news products slick slider 
        new_products = products.filter(is_published=True).order_by('-created_at')[:3]

        for item in products:
            if item.marka.all():
                marka = True
            if item.color_title:
                color_title = True
            if item.internal_storage:
                internal_storage = True
            if item.is_new:
                condition = True
            if item.operator_code != None:
                operator = True
            # if item.is_new == True:
            else:
                operator_data = item.operator_code

        # for paginator customize
        page = self.request.GET.get('page')
        paginator = Paginator(products, 20)
        print(paginator, 'psginator')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {
            'customer': customer,
            'order': order,
            'products': products,
            'categories': category,
            'marka': marka,
            'markas': markas,
            'color_title': color_title,
            'internal_storage': internal_storage,
            'internal_storages': internal_storages,
            'colors': colors,
            'condition': condition,
            'operator': operator,
            'operator_data': operator_data,
            'operators_codes': operators_codes,
            'new_products': new_products,
        }
        print(context)
        return context

    # def get_queryset(self):
    #     queryset = super(ProductsListView, self).get_queryset()

    #     slug = self.kwargs['slug']
    #     category = get_object_or_404(Category, slug=slug)
    #     queryset = Product.objects.filter(category=category).filter(is_published=True)
    #     # if self.request.GET.get('slug'):
    #         # queryset_list = queryset_list.filter(category__slug=self.request.GET.get('slug'))
    #         # queryset = 
    #     return queryset
