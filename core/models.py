from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Review(models.Model):
  title = models.CharField(max_length=300)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)
  def get_absolute_url(self):
    return reverse("review_detail", args=[self.id])

  def __unicode__(self):
    return self.title

class Comment(models.Model):
    review = models.ForeignKey(Review)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __unicode__(self):
        return self.text