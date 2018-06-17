from django.contrib import admin

from .models import Category, Service, Plan


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]

    class Meta:
        model = Service


admin.site.register(Service, ServiceAdmin)


class PlanAdmin(admin.ModelAdmin):
    class Meta:
        model = Plan


admin.site.register(Plan)
