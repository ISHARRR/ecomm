from django.db import models
import random
import os

# Create your models here.


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

    def active(self):
        return self.filter(active=True)


class ProductModelManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def features(self):
        return self.get_queryset().featured()

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

    objects = ProductModelManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)

    def __str__(self):
        return self.title
