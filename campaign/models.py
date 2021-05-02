from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.conf import settings

class Categories(models.TextChoices):
    SOCIAL = 'social'
    ANTI_DRUG = 'anti-drug'
    DOMESTIC_VOILENCE = 'domestic-voilence'
    RACIAL_DISCRIMINATION = 'racial-discrimination'
    BULLYING = 'bullying'
    ANTI_BEGGARY = 'anti-beggary'
    ANTI_RAPE = 'anti-rape'
    ANTI_ABORTION = 'anti-abortion'
    ANTI_GAMBLING = 'anti-gambling'
    CLIMATE_CHANGE = 'climate-change'

class CampaignPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.SOCIAL)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    event_date = models.DateTimeField(default=datetime.now, blank=True)
    event_location = models.CharField(max_length=150, null=True)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = CampaignPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = CampaignPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = CampaignPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except CampaignPost.DoesNotExist:
                pass
        
        super(CampaignPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title