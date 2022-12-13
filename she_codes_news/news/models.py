from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=1000, default="https://cdn.browshot.com/static/images/not-found.png" ) #default if no image put this image
    #author = models.CharField(max_length=200)
    author =models.ForeignKey(
        USER, on_delete=models.CASCADE
    )

    pub_date = models.DateTimeField()
    content = models.TextField()
