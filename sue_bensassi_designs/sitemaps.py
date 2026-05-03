from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'

    _items = {
        'home':           1.0,
        'products':       0.9,
        'about':          0.7,
        'contact':        0.7,
        'delivery':       0.7,
        'terms':          0.5,
        'cookie_policy':  0.5,
        'privacy_policy': 0.5,
    }

    def items(self):
        return list(self._items.keys())

    def priority(self, item):
        return self._items[item]

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return reverse('product_detail', args=[obj.id])
