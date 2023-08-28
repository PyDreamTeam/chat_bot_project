from .models import SolutionGroup, SolutionFilter, SolutionTag, Solution
from django.contrib import admin

admin.site.register(SolutionGroup)
admin.site.register(SolutionFilter)
admin.site.register(SolutionTag)
admin.site.register(Solution)

