from django.http import Http404
from django.views.generic import ListView, DetailView
# Create your views here.

from . models import ProductModel
from carts.models import Cart


class ProductFeatured(ListView):
    template_name = "home_page.html"

    def get_queryset(self, *args, **kwargs):
        return ProductModel.objects.all().active().featured()


class ProductSale(ListView):
    template_name = "sale.html"

    def get_queryset(self, *args, **kwargs):
        return ProductModel.objects.all().active().sale()


class ProductList(ListView):
    template_name = "products/product_list.html"

    def get_queryset(self):
        obj = ProductModel.objects.all()
        return obj


class ProductDetailSlug(DetailView):
    queryset = ProductModel.objects.all()
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailSlug, self).get_context_data(**kwargs)
        cart_object, new_object = Cart.objects.new_get(self.request)
        context['cart'] = cart_object
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get("slug")
        try:
            obj = ProductModel.objects.get(slug=slug, active=True)
        except ProductModel.DoesNotExist:
            raise Http404("Does not exist")
        except ProductModel.MultipleObjectsReturned:
            qs = ProductModel.objects.filter(slug=slug, active=True)
            obj = qs.first()
        except:
            raise Http404("da ppaccck")
        return obj


# def product_list(request):
#     filter_qs = ProductFilter(request.GET, queryset=ProductModel.objects.all())
#     return render(request, 'sale.html', {'filter': filter_qs})


class ProductDetail(DetailView):
    # queryset = ProductModel.objects.all()
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)

        return context

    def get_queryset(self, *args, **kwargs):
        # request = self.request
        pk = self.kwargs.get("pk")
        return ProductModel.objects.filter(pk=pk)

