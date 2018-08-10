from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=120, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    date = models.DateTimeField(verbose_name="Creation date")

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"article_id": self.id})
