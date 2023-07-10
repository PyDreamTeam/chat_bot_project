from django.contrib import admin
from solutions.models import Solutions, Solution_filters, Filter_solutions

@admin.register(Solutions)
class SolutionsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "platform",
        "image",
        "short_description",
        "full_description",
        "price",
        "created_at",
    ]


@admin.register(Solution_filters)
class SolutionsFiltersAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "properties",
    ]


@admin.register(Filter_solutions)
class FilterSolutionsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "solution",
        "filter_solution",
    ]