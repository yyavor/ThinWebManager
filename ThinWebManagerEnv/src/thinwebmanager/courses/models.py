from django.db import models
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"course_id": self.id})
