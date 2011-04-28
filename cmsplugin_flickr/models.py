from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin

ALL_TAGS = 'all'
ANY_TAG = 'any'
TAG_MODE_CHOICES = ((ANY_TAG, _('Any Tag')),
                    (ALL_TAGS, _('All Tags')))

DATE_POSTED_ASC = 'date-posted-asc'
DATE_POSTED_DESC = 'date-posted-desc'
DATE_TAKEN_ASC = 'date-taken-asc' 
DATE_TAKEN_DESC = 'date-taken-desc'
INTERESTINGNESS_ASC = 'interestingness-asc' 
INTERESTINGNESS_DESC = 'interestingness-desc'
RELEVANCE = 'relevance'
ORDER_CHOICES =((DATE_POSTED_ASC, _('Date Posted Ascending')),
                (DATE_POSTED_DESC, _('Date Posted Descending')),
                (DATE_TAKEN_ASC, _('Date Taken Ascending')),
                (DATE_TAKEN_DESC, _('Date Taken Descending')),
                (INTERESTINGNESS_ASC, _('Interestingness Ascending')),
                (INTERESTINGNESS_DESC, _('Interestingness Descending')),
                (RELEVANCE, _('Relevance')))

SMALL_SQUARE = 's'
THUMBNAIL = 't'
SMALL = 'm'
MEDIUM = '-'
LARGE = 'b'
ORIGINAL = 'o'
SIZE_CHOICES = (('s', _('Small Square 75px x 75px')),
                ('t', _('Thumbnail, 100px on longest side')),       
                ('m', _('Small, 240px on longest side')),
                ('-', _('Medium, 500px on longest side')),
                ('b', _('Large, 1024px on longest side')),
                ('o', _('Original image, either a jpg, gif or png')))


class Flickr(CMSPlugin): 
    title = models.CharField(max_length=100)
    show_title = models.BooleanField(default=True)
    count = models.PositiveIntegerField(default=10,
                                        help_text=_('Number of images to be displayed'))
    user_name = models.CharField(max_length=50,
                                 help_text=_('User name to get images from.'),
                                 blank=True)
    group_id = models.CharField(max_length=50,
                                help_text=_('Get images only from this group.'),
                                blank=True)
    tags = models.CharField(max_length=50, blank=True,
                            help_text=_('Get only images with these tags (seperate via comma ",").'))
    tags_match = models.CharField(choices=TAG_MODE_CHOICES,
                                  max_length=3,
                                  default=ANY_TAG,
                                  help_text=_('Match all tags or any.'))
    size = models.CharField(choices=SIZE_CHOICES,
                            max_length=1, default=SMALL_SQUARE)
    order = models.CharField(choices=ORDER_CHOICES,
                             default=RELEVANCE,
                             max_length=50)


    class Meta:
        verbose_name=_('Flickr CMS Plugin')
        
    def __unicode__(self):
        return self.title
    