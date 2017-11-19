# -*- coding: utf-8 -*-
from rest_framework import serializers, pagination
from stock.models import Producto, Categoria, Marca, UnidadMedida, Inventario


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre', )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nombre', )


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadMedida
        fields = ('id', 'nombre', )


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventario
        fields = ('id', 'sucursal', 'codigo_barra', 'nombre','categoria', 'marca', 'unidad_medida', 'precio_compra',
                  'porcentaje_ganacia', 'get_precio_compra', 'get_porcentaje_ganacia', 'stock_actual', 'stock_minimo',
                  'stock_maximo', 'estante', 'fila', 'columna')


class PaginatedInventorySerializer(pagination.PageNumberPagination):
    class Meta:
        object_serializer_class = InventorySerializer


class ProductSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField(many=False)
    marca = serializers.StringRelatedField(many=False)
    unidad_medida = serializers.StringRelatedField(many=False)

    class Meta:
        model = Producto
        fields = ('id', 'codigo_barra', 'nombre', 'categoria', 'marca', 'unidad_medida', 'precio_compra',
                  'porcentaje_ganacia')


class PaginatedProductSerializer(pagination.PageNumberPagination):
    class Meta:
        object_serializer_class = ProductSerializer


class ProductAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', )