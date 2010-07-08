
from django.utils.translation import gettext as _
from django.conf import settings

import flickrapi

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import *

FLICKR_IMAGE_URL = "http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s_%(size)s.jpg"
FLICKR_URL = "http://www.flickr.com/photos/%(user_id)s/%(id)s"
FLICKR_GROUP_URL = "http://www.flickr.com/groups/%(id)s"

class FlickrPlugin(CMSPluginBase):
    model = Flickr
    name = _("Flickr")
    admin_preview = False     
    render_template = "cms_plugins/flickr_cms_plugin.html" 
    
    def render(self, context, instance, placeholder):
        items = []
        try:
            f = flickrapi.FlickrAPI(settings.FLICKR_API_KEY,
                   settings.FLICKR_API_SECRET)
            kwargs = {'sort': instance.order,
                      'per_page': instance.count}
            if instance.user_name:
                rsp = f.people_findByUsername(username=instance.user_name)
                user_id = [x for x in rsp][0].attrib['id']
                kwargs.update({'user_id': user_id})   
                url = FLICKR_URL                
            if instance.tags:
                kwargs.update({'tags': instance.tags,
                               'tag_mode': instance.tags_match})
            if instance.group_id:
                kwargs.update({'group_id': instance.group_id})
                if not instance.user_name:
                    url = FLICKR_GROUP_URL
            photos = f.photos_search(**kwargs)[0]
            for p in photos:
                p.attrib['size'] = instance.size
                if not instance.user_name:
                    id = instance.group_id
                else:
                    id = p.attrib['id']
                items.append({'title': p.attrib['title'],
                              'url': FLICKR_IMAGE_URL % p.attrib,
                              'link': url % {'user_id': user_id,
                                                   'id': id}})
        except flickrapi.FlickrError, e:
            error = "FlickrAPI Error: " + str(e)
            print error
            context.update({'flickr_error': error})
            
        context.update({'object': instance,
                        'items': items,
                        'placeholder': placeholder})
        return context
      
plugin_pool.register_plugin(FlickrPlugin)