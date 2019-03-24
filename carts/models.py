from django.db import models
from django.conf import settings
from products.models import ProductModel
from django.db.models.signals import pre_save, post_save, m2m_changed
# Create your models here.


User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_get(self, request):
        cart_id = request.session.get('cart_id', None)
        queryset = self.get_queryset().filter(id=cart_id)
        if queryset.count() == 1:
            new_object = False
            cart_object = queryset.first()
            if request.user.is_authenticated and cart_object.user is None:
                cart_object.user = request.user
                cart_object.save()
        else:
            cart_object = Cart.objects.new_cart(user=request.user)
            new_object = True
            request.session['cart_id'] = cart_object.id
        return cart_object, new_object

    def new_cart(self, user=None):
        user_object = None
        if user is not None:
            if user.is_authenticated:
                user_object = user
        return self.model.objects.create(user=user_object)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductModel, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=100000, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100000, decimal_places=2)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


def m2m_save_cart_r(instance, action, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        product = instance.product.all()
        total = 0
        for prod in product:
            total += prod.price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(m2m_save_cart_r, sender=Cart.product.through)


def pre_save_cart(instance, **kwargs):
    if instance.subtotal > 0:
        instance.total = instance.subtotal
    else:
        instance.total = 0.00


pre_save.connect(pre_save_cart, sender=Cart)
