from django.contrib.auth.models import User
from django.db import models

from common.models import BaseModel
from post.models import Post


class Chat(BaseModel):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")

    def __str__(self) -> str:
        return self.post.title


class ChatMessage(BaseModel):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    message = models.TextField()

    def __str__(self):
        return self.message
