from django.conf.urls import url
from .views import ProductListView, ProductDetailView, ProductAutocompleteView, CategoryListView, BrandListView, \
    MeasureListView

urlpatterns = [
    url(r'^product$', ProductListView.as_view(), name='api_product_list'),
    url(r'^product/(?P<pk>[0-9]+)$', ProductDetailView.as_view(), name='api_product_detail'),
    url(r'^product/autocomplete$', ProductAutocompleteView.as_view(), name='api_product_autocomplete'),

    url(r'^category$', CategoryListView.as_view(), name='api_category_list'),
    url(r'^brand$', BrandListView.as_view(), name='api_brand_list'),
    url(r'^measure$', MeasureListView.as_view(), name='api_measure_list'),


]