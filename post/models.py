from django.contrib.auth.models import User
from django.db import models

from common.models import BaseModel
from option.models import PostOption
from plan.models import PlanDetail

PRICE, FREE, EXCHANGE = ("Price", "Free", "Exchange")

ACTIVE, INACTIVE, PROCESS, NOTPAYED = ("Active", "Inactive", "Process", "Not Payed")


class Category(BaseModel):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="categories")
    order = models.IntegerField(default=0)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    # options = models.ManyToManyField(Option)

    def __str__(self):
        return self.title


class SubCategory(BaseModel):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')

    # options = models.ManyToManyField(Option)

    def __str__(self):
        return self.title


class Region(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class District(BaseModel):
    title = models.CharField(max_length=128)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='district')

    def __str__(self):
        return self.title


class Post(BaseModel):
    PRICE_TYPE = ((PRICE, PRICE), (FREE, FREE), (EXCHANGE, EXCHANGE))

    STATUS = (
        (ACTIVE, ACTIVE),
        (INACTIVE, INACTIVE),
        (PROCESS, PROCESS),
        (NOTPAYED, NOTPAYED),
    )

    title = models.CharField(max_length=256)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='post')
    plan = models.ForeignKey(PlanDetail, on_delete=models.CASCADE, related_name='plans')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    content = models.TextField()
    main_photo = models.ImageField(upload_to="post/")
    price_type = models.CharField(max_length=256, choices=PRICE_TYPE)
    price = models.PositiveIntegerField(default=0, null=True)
    status = models.CharField(max_length=256, choices=STATUS)
    views_count = models.IntegerField(default=0)

    json = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title

    def make_json_fields(self):
        data = {
            "title": "",
            "extended_title": "",
            "year": "",
            "model": "",
            "district": "",
            "photos_count": 0,
            "options": [],
        }
        data.update(**PostOption.generate_json_options(self.id))
        data["district"] = self.district.title
        data["photos_count"] = self.photos.count()
        data["title"] = f"{data['model']}"
        return data


class PostPhotos(BaseModel):
    image = models.ImageField(upload_to="post/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="photos")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.order

    @classmethod
    def get_main_photo(cls, post_id):
        photo = PostPhotos.objects.filter(post_id=post_id, is_main=True).first()
        print(photo)
        if photo:
            return photo.image
        return None
