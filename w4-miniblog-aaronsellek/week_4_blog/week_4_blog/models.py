from django.db import models
from django.urls import reverse
import datetime

class Posts(models.Model):
    name = models.CharField(max_length=300, help_text="Enter a title for your blog: )")
    content = models.TextField(max_length=10000, help_text='Write post here.')
    post_date = models.DateField(default=datetime.date.today)
    topic = models.ManyToManyField(Topic, help_text='Select the topic for this post.')

class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse("(blogpost-detail)", args=[str(self.id)])

