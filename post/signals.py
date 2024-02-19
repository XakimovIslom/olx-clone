from django.db.models.signals import post_save
from django.dispatch import receiver
from post.models import PostPhotos


@receiver(post_save, sender=PostPhotos)
def post_save__post_option(sender, instance, created, **kwargs):
    instance.post.json = instance.post.make_json_fields()
    instance.post.main_photo = PostPhotos.get_main_photo(instance.post.id)
    instance.post.save()