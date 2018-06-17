from rest_framework import serializers

from .models import Category, Service, Plan, Work


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'description', 'category', 'photo', 'date', 'provide', 'plan', 'owner', 'time_coins')


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


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('id', 'service', 'worker', 'status', 'feedback')
