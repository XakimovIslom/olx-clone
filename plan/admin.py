from django.contrib import admin
from plan.models import OptionTypePlan, PlanDetailGroup, PlanDetail, PlanDetailPrice, Plan, PlanPrice

# admin.site.register(OptionTypePlan)
admin.site.register(PlanDetailGroup)
admin.site.register(PlanDetail)
admin.site.register(PlanDetailPrice)
admin.site.register(Plan)
admin.site.register(PlanPrice)
