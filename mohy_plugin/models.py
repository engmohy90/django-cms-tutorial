from django.db import models
from cms.models.pluginmodel import CMSPlugin


class Daily_Specials(CMSPlugin):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="daily_specials")
    description = models.TextField()

    class Meta:
        verbose_name = "Daily Special"
        verbose_name_plural = "Daily Special"

    def __unicode__(self):

        return "%s" %(self.name)