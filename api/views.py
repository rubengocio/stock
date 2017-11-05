# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ProductSerializer, CategorySerializer, MeasureSerializer, BrandSerializer
from stock.models import Producto, Categoria, UnidadMedida, Marca


class ProductAutocompleteView(APIView):
    def get(self, request):
        queryset = Producto.objects.all()
        query = request.GET.get('query', None)
        if query:
            queryset = queryset.filter(nombre__contains=query)

        result = []

        for row in queryset:
            result.append({'id': row.id, 'value': row.nombre})

        return Response(result)


class ProductListView(ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = self.queryset
        bar_code = self.request.GET.get('bar_code', None)
        product = self.request.GET.get('product', None)
        category = self.request.GET.get('category', None)
        brand = self.request.GET.get('brand', None)
        measure = self.request.GET.get('measure', None)

        if bar_code:
            queryset = queryset.filter(codigo_barra=bar_code)

        if product:
            queryset = queryset.filter(nombre__contains=product)

        if category:
            queryset = queryset.filter(categoria__id=category)

        if brand:
            queryset = queryset.filter(marca__id=brand)

        if measure:
            queryset = queryset.filter(unidad_medida__id=measure)

        return queryset


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer


class CategoryListView(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategorySerializer


class MeasureListView(ListCreateAPIView):
    queryset = UnidadMedida.objects.all()
    serializer_class = MeasureSerializer


class BrandListView(ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = BrandSerializer