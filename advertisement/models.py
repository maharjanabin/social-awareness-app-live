
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.conf import settings


class AdvertisementPost(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    slug = models.SlugField()
    poster = models.ImageField(upload_to='photos/%Y/%m/%d/')
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = AdvertisementPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = AdvertisementPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug
        
        super(AdvertisementPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title