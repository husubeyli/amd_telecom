from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView

# Create your views here.
from django.http import HttpResponse
from .models import Product, Product_images, Product_details, Category
from order.models import OrderItem, Order
from account.models import Customer



class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    # context_object_name = 'products'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        details = Product_details.objects.all()

        context["products"] = products
        context['detauls'] = details
        return context
    




# def product_detail(request, pk):
#     product = Product.objects.get(id=pk)
#     print(product, 'belkem')
#     photos = Product_images.objects.filter(product=product)
#     print(photos, 'necelilk')
#     details = Product_details.objects.filter(product=product)

#     if request.method == 'POST':
#         product = Product.objects.get(id=pk)
#         device = request.COOKIES['device']
#         customer, created = Customer.objects.get_or_create(device=device)

#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
#         orderItem.quantity=request.POST['quantity']
#         orderItem.save()

#         return redirect('cart')
#     context = {
#         'product': product, 
#         'photos': photos, 
#         'details': details,
#     }
#     return render(request, 'product_detail.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # product = get_object_or_404(Product, id=self.kwargs['pk'])
        product = Product.objects.get(slug=self.object.slug)
        print(product, 'salas')
        # photos = get_object_or_404(Product_images, product=product)
        photos = Product_images.objects.filter(product=product)
        details = Product_details.objects.filter(product=product)
        context['product'] = product
        context['photos'] = photos
        context['details'] = details
        print(details, 'sekilci')
        return context

    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()
    

# class CategoryListView(ListView):
#     model = Category
#     context_object_name = 'category_list'
#     template_name = 'base.html'
#     queryset = Category.objects.filter(status=True)



class ProductsFilterListView(ListView):
    model = Product
    template_name = 'products.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        products = Product.objects.filter(category=category)
        context["category"] = get_object_or_404(Category, slug=self.kwargs['slug'])
        context = {
        'products': products,
        'categories': category
        }
        return context

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        queryset = Product.objects.filter(category=category).filter(is_published=True)
        return queryset


# def product_filter(request, slug):
#     print(slug, 'belede')
#     category = Category.objects.get(slug=slug)
#     print(category, 'belede')
#     products = Product.objects.filter(category=category).first()
#     print(products, 'elcn')
#     context = {
#         'products_list': products,
#         'categories': category
#     }
#     return render(request, 'products.html', context)