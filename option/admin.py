from django.contrib import admin
from option.models import Option, OptionValue, PostOption, PostOptionValue

admin.site.register(Option)
admin.site.register(OptionValue)
admin.site.register(PostOption)
admin.site.register(PostOptionValue)
