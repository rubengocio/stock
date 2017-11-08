
from django.conf.urls import url
from .views.providers import ProviderListView, ProviderCreateView, ProviderUpdateView, ProviderDeleteView
from .views.clients import ClientCreateView, ClientListView, ClientUpdateView, ClientDeleteView,  home
from .views.categories import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from .views.brands import BrandListView, BrandCreateView, BrandUpdateView, BrandDeleteView
from .views.measurements import MeasurementListView, MeasurementCreateView, MeasurementUpdateView, MeasurementDeleteView
from .views.products import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from .views.imports import upload
from .views.box_daily import BoxView

urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^importar-exportar-productos/$', upload, name='import-export'),

    url(r'^listar-productos/$',ProductListView.as_view(), name='product-list'),
    url(r'^crear-producto/$',ProductCreateView.as_view(), name='product-create'),
    url(r'^editar-producto/(?P<pk>\d+)$',ProductUpdateView.as_view(), name='product-edit'),
    url(r'^eliminar-producto/(?P<pk>\d+)$',ProductDeleteView.as_view(), name='product-remove'),

    url(r'^listar-proveedores/$',ProviderListView.as_view(), name='provider_list'),
    url(r'^crear-proveedor/$',ProviderCreateView.as_view(), name='provider'),
    url(r'^editar-proveedor/(?P<pk>\d+)$',ProviderUpdateView.as_view(), name='provider-detail'),
    url(r'^elimnar-proveedor/(?P<pk>\d+)$',ProviderDeleteView.as_view(), name='provider-remove'),

    url(r'^listar-clientes/$', ClientListView.as_view(), name='client-list'),
    url(r'^crear-cliente/$', ClientCreateView.as_view(), name='client-create'),
    url(r'^editar-cliente/(?P<pk>\d+)$', ClientUpdateView.as_view(), name='client-edit'),
    url(r'^eliminar-cliente/(?P<pk>\d+)$', ClientDeleteView.as_view(), name='client-remove'),

    url(r'^listar-categorias/$', CategoryListView.as_view(), name='category-list'),
    url(r'^crear-categoria/$', CategoryCreateView.as_view(), name='category-create'),
    url(r'^editar-categoria/(?P<pk>\d+)$', CategoryUpdateView.as_view(), name='category-edit'),
    url(r'^eliminar-categoria/(?P<pk>\d+)$', CategoryDeleteView.as_view(), name='category-remove'),

    url(r'^listar-marcas/$', BrandListView.as_view(), name='brand-list'),
    url(r'^crear-marca/$', BrandCreateView.as_view(), name='brand-create'),
    url(r'^editar-marca/(?P<pk>\d+)$', BrandUpdateView.as_view(), name='brand-edit'),
    url(r'^eliminar-marca/(?P<pk>\d+)$', BrandDeleteView.as_view(), name='brand-remove'),

    url(r'^listar-medida/$', MeasurementListView.as_view(), name='measurement-list'),
    url(r'^crear-medida/$', MeasurementCreateView.as_view(), name='measurement-create'),
    url(r'^editar-medida/(?P<pk>\d+)$', MeasurementUpdateView.as_view(), name='measurement-edit'),
    url(r'^eliminar-medida/(?P<pk>\d+)$', MeasurementDeleteView.as_view(), name='measurement-remove'),

    url(r'^caja-diaria/$', BoxView.as_view(), name='box-daily'),
]
