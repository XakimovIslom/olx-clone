from django.contrib import admin

from post.models import Category, Post, Region, District, SubCategory

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(SubCategory)
