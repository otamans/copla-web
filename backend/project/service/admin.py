from profile import Profile

from django.contrib import admin

from .models import Category, Service, Plan


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


class ServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Service


class PlanAdmin(admin.ModelAdmin):
    class Meta:
        model = Plan


class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Plan, PlanAdmin)
