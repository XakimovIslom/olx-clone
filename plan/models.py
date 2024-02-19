from django.db import models
from common.models import BaseModel


class OptionTypePlan(models.TextChoices):
    SELECT_BUTTON = "7"
    SELECT_BUTTON2 = "30"


class PlanDetailGroup(BaseModel):
    title = models.CharField(max_length=256)
    is_multiple = models.BooleanField(default=False)
    text = models.CharField(max_length=15)

    def __str__(self):
        return self.title


TOP, UP, VIP = ("TOP", "Teapaga chiqarish", "VIP")


class PlanDetail(BaseModel):

    STATUS = (
        (TOP, TOP),
        (UP, UP),
        (VIP, VIP),
    )
    group_id = models.ForeignKey(PlanDetailGroup, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=256, choices=STATUS, null=True, blank=True)
    choice_text = models.CharField(max_length=128, choices=OptionTypePlan.choices)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.choice_text


class PlanDetailPrice(BaseModel):
    plan_detail = models.ForeignKey(PlanDetail, on_delete=models.CASCADE)
    category = models.CharField(max_length=128)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.category


class Plan(BaseModel):
    title = models.CharField(max_length=256)
    plan_detail = models.ManyToManyField(PlanDetail)

    def __str__(self):
        return self.title


class PlanPrice(BaseModel):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    category = models.CharField(max_length=128)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.plan.title
