from product.models import Product
from product.models import Product_details, Category
from django.views.generic import TemplateView


# Create your views here.


# def home_page(request):
#     products = Product.objects.all()
#     category = Category.objects.all()
#     details = Product_details.objects.all()
#     context = {'products':products, 'details': details,'category':category }
#     return render(request, 'home.html', context)


class HomePageTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        category = Category.objects.all()
        details = Product_details.objects.all()
        context["products"] = products
        context["details"] = details
        context["category"] = category
        return context
    
