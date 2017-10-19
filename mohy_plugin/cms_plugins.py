from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *
from django.utils.translation import ugettext_lazy as _


class Daily_Special_Plugin(CMSPluginBase):
    model = Daily_Specials
    name = "Daily Specials"
    render_template = "daily_specials.html"

    def render(self, context, instance, placeholder):
        context.update({
            'name': instance.name,
            'image': instance.image,
            'description': instance.description,

        })
        return context


plugin_pool.register_plugin(Daily_Special_Plugin)
