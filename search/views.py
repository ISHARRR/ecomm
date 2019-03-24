from django.views.generic import ListView
from products.models import ProductModel
from django.db.models import Q
# Create your views here.


class SearchProducts(ListView):
    template_name = "search/search.html"

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query is not None:
            return ProductModel.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).active().distinct()
        return ProductModel.objects.none()
