from .models import Category, Service, Plan, Work
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'description', 'category', 'photo', 'date', 'provide', 'plan', 'owner', 'time_coins')


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


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'
