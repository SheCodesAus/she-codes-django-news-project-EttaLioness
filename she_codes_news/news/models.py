from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
class NewsStory(models.Model):
    class Meta: 
        ordering = ["-pub_date"]
        verbose_name_plural = "News Stories"

    title = models.CharField(max_length=200)
    image = models.URLField(max_length=1000, default="https://cdn.browshot.com/static/images/not-found.png" ) #default if no image put this image
    #author = models.CharField(max_length=200)
    author =models.ForeignKey(
        USER, on_delete=models.CASCADE
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="stories",blank=True,null=True)
    pub_date = models.DateTimeField()
    content = models.TextField()
    favourited_by = models.ManyToManyField(USER, related_name='favourites', blank=True, null=True ) 