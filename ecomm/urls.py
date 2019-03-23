"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.contrib.auth.views import (
    LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import path, re_path
from . views import home_page, login_page, about_page, register_page, profile, update_password, update_profile
from contact.views import contact
from products.views import (ProductListView,
                            ProductDetailView,
                            ProductDetailSlugView,
                            ProductFeaturedDetailView,
                            ProductFeaturedListView,
                            )

from search.views import (SearchProductListView)
from carts.views import (cart_yard, cart_update)

urlpatterns = [
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('contact/', contact, name="contact_us"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('products/', ProductListView.as_view(), namespace="products"),
    path('products/', ProductListView.as_view(), name="products"),
    path('search/', SearchProductListView.as_view(), name="search"),
    re_path(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='prod_detail'),
    path('cart/', cart_yard, name="cart"),
    path('cart-update/', cart_update, name="cart_update"),
    path('change-password/', update_password, name='update_password'),
    path('password/', update_password, name='password'),
    path('profile/', profile, name='profile'),
    path('update-profile/', update_profile, name='update_profile'),
    path('forgotten-password', PasswordResetView.as_view(template_name='reset_pass.html'), name='reset_pass'),
    path('forgotten-password/email-sent', PasswordResetDoneView.as_view(template_name='email_sent.html'),
         name='password_reset_done'),
    re_path('reset-password/confirm(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)',
            PasswordResetConfirmView.as_view(template_name='set_pass.html'),name='password_reset_confirm'),
    path('reset-password/complete', PasswordResetCompleteView.as_view(template_name='pass_reset_complete.html'),
         name='password_reset_complete'),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    # path('products/<int:pk>/', ProductDetailView.as_view()),


    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "ISHAR's Admin"
admin.site.site_title = "ISHAR's Admin Portal"
admin.site.index_title = "Welcome to ISHAR's Researcher Portal"