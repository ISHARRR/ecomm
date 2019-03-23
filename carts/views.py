from django.shortcuts import render, redirect
from . models import Cart
from products.models import ProductModel


# Create your views here.


def cart_yard(request):
    obj, new_objects = Cart.objects.new_get(request)
    # context = { "cart": obj }
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
    return render(request, 'carts/yard.html', {'cart': obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        product_object = ProductModel.objects.get(id=product_id)
        cart_object, new_object = Cart.objects.new_get(request)
        if product_object in cart_object.product.all():
            cart_object.product.remove(product_object)
        else:
            cart_object.product.add(product_object)
        request.session["cart_total"] = cart_object.product.count()
    return redirect('home')
