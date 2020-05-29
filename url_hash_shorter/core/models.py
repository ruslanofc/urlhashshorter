import hashlib
import secrets
import string

from django.db import models
from django.urls import reverse


class URL(models.Model):

    source_url = models.URLField(unique=True)
    short_slug = models.SlugField(max_length=64, default=None, unique=True)
    salt = models.CharField(default=None, max_length=10)
    views = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('core:url_redirect', args=(str(self.short_slug),))

    def save(self, *args, **kwargs):
        alphabet = string.ascii_letters + string.digits
        if self.short_slug is None:
            while True:
                salt = ''.join(secrets.choice(alphabet) for i in range(URL._meta.get_field('salt').max_length))
                slug = hashlib.pbkdf2_hmac('sha256', self.source_url.encode('utf-8'), salt.encode('utf-8'), 100000).hex()
                if URL.objects.filter(short_slug=slug).exists():
                    continue
                self.salt = salt
                self.short_slug = slug
                break
        super(URL, self).save(*args, **kwargs)
