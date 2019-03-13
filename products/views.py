from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

from . models import ProductModel


class ProductFeaturedListView(ListView):
    template_name = "products/product_list.html"

    def get_queryset(self, *args, **kwargs):
        return ProductModel.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured_detail.html"

    def get_queryset(self, *args, **kwargs):
        return ProductModel.objects.all().featured()


class ProductListView(ListView):
    template_name = "products/product_list.html"

    def get_queryset(self):
        obj = ProductModel.objects.all()
        return obj


class ProductDetailSlugView(DetailView):
    queryset = ProductModel.objects.all()
    template_name = "products/product_detail.html"

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


class ProductDetailView(DetailView):
    # queryset = ProductModel.objects.all()
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)

        return context

    def get_queryset(self, *args, **kwargs):
        # request = self.request
        pk = self.kwargs.get("pk")
        return ProductModel.objects.filter(pk=pk)
