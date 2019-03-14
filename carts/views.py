from django.shortcuts import render, redirect
from . models import Cart
from products.models import ProductModel


# Create your views here.


def cart_yard(request):
    # obj, new_objects = Cart.objects.new_get(request)
    # # cart_id = request.session.get('cart_id', None)
    # # # if cart_id is None and isinstance('cart_id', int):
    # # #     obj = Cart.objects.create(user=None)
    # # #     request.session['cart_id']= cart_id.id
    # # # else:
    # # qs = Cart.objects.filter(id=cart_id)
    # # if qs.count() == 1:
    # #     obj = qs.first()
    # #     if request.user.is_authenticated and obj.user is None:
    # #         obj.user = request.user
    # #         obj.save()
    # # else:
    # #     obj = Cart.objects.new_cart(user=request.user)
    # #     request.session['cart_id'] = obj.id
    #
    # products = obj.products.all()
    # for product in products:
    #     total += product.price
    return render(request, 'carts/yard.html')


def cart_update(request):
    product_id = 1
    product_object = ProductModel.objects.get(id=product_id)
    cart_object, new_object = Cart.objects.new_get(request)
    cart_object.product.add(product_object)
    return redirect('cart')
