from django.db import models

from common.models import BaseModel


class OptionType(models.TextChoices):
    SELECT_BUTTON = "Select_Button"
    NUMBER = "Number"
    SELECT = "Select"
    TEXT = "Text"
    MULTIPLE_CHOICE = "Multiple choice"


class Option(BaseModel):
    title = models.CharField(max_length=256)
    type = models.CharField(max_length=15, choices=OptionType.choices)
    order = models.IntegerField(default=0)
    # regex =
    limit = models.IntegerField(null=True, blank=True)
    place_holder = models.CharField(max_length=128, null=True, blank=True)
    is_required = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class OptionValue(BaseModel):
    option = models.ForeignKey(
        Option, on_delete=models.CASCADE, related_name="values"
    )
    value = models.CharField(max_length=256)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.value


class PostOption(BaseModel):
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE, related_name="options")
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="posts")
    value = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"{self.post} {self.option}"

    @classmethod
    def generate_json_options(cls, post_id):
        data = {"options": []}
        post_options = (
            cls.objects.filter(post_id=post_id)
            .order_by("option__order")
            .select_related(
                "option",
            )
            .prefetch_related("values")
            .prefetch_related(
                "values", "values__option_value",
            )
        )
        for post_option in post_options:
            data["options"].append(
                {
                    "title": post_option.option.title,
                    "value": post_option.value,
                    "values": [
                        values.option_value.value for values in post_option.values.all()
                    ],
                }
            )
            if post_option.option.code == "year":
                data["year"] = post_option.value
            if post_option.option.code == "model":
                for value in post_option.values.all():
                    if value.option_value_extended:
                        if value.option_value_extended.parent:
                            data["model"] = (
                                f"{value.option_value.value} {value.option_value_extended.parent.value}, "
                                f"{value.option_value_extended.value}"
                            )
                        else:
                            data["model"] = (
                                f"{value.option_value.value} {value.option_value_extended.value}"
                            )
                    else:
                        data["model"] = value.option_value.value
        return data


class PostOptionValue(BaseModel):
    post_option = models.ForeignKey(
        PostOption, on_delete=models.CASCADE, related_name="values"
    )
    option_value = models.ForeignKey(OptionValue, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ("post_option", "option_value")
