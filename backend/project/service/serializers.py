from .models import Category, Service, Plan
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'description', 'category', 'photo', 'date', 'provide', 'plan')


class CategorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'services')


class PlanSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        fields = ('id', 'name', 'description', 'services')
