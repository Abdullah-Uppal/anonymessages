from django.core.exceptions import ImproperlyConfigured
from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.http import request
from django.urls.base import reverse
from django.utils import timezone
from django.contrib.sites.shortcuts import get_current_site

class URL(models.Model):
  name = models.CharField(max_length=30)
  url = models.URLField(null=False, blank=False)
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
  time_created = models.DateTimeField(default=timezone.now)

  def __str__(self) -> str:
      return self.name
    
  def get_absolute_url(self):
    return reverse('home')

class AnonymousMessage(models.Model):
  message = models.TextField(help_text="Send your message anonymously.")
  to = models.ForeignKey(URL, on_delete=models.CASCADE)
  time_created = models.DateTimeField(default=timezone.now)

  def __str__(self) -> str:
      return self.message[:30]
