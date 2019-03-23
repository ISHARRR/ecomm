from django.db import models
import random
import os
import django_filters

# Create your models here.
from django.forms import forms
from django.urls import reverse


def get_filename_extension(filepath):
    org_name = os.path.basename(filepath)
    name, ext = os.path.splitext(org_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,100000)
    name, ext = get_filename_extension(filename)
    final_filename = f'{new_filename}{ext}'
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

    def sale(self):
        return self.filter(sale=True)

    def active(self):
        return self.filter(active=True)


class ProductModelManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def features(self):
        return self.get_queryset().featured()

    def sales(self):
        return self.get_queryset().sale()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    sale = models.BooleanField(default=False)

    objects = ProductModelManager()

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug=self.slug)
        return reverse("prod_detail", kwargs={"slug":self.slug})

    def __str__(self):
        return self.title


# class ProductFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     price = django_filters.CharFilter(lookup_expr='iexact')
#     description = django_filters.CharFilter(lookup_expr='icontains')
#
#     class Meta:
#         model = ProductModel
#         exclude = ['image']
#         fields = ['title', 'price', 'description', ]

#
# class ProductFilter(django_filters.FilterSet):
#     class Meta:
#         model = ProductModel
#         fields = ['title', 'price']
#         filter_overrides = {
#             models.CharField: {
#                 'filter_class': django_filters.CharFilter,
#                 'extra': lambda f: {
#                     'lookup_expr': 'icontains',
#                 },
#             },
#             models.BooleanField: {
#                 'filter_class': django_filters.BooleanFilter,
#                 'extra': lambda f: {
#                     'widget': forms.CheckboxInput,
#                 },
#             },
#
#        },

