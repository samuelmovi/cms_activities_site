from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from contact_bar_plugin.models import Contact
from photo_carousel_plugin.models import CarouselPhoto
from text_bubble_plugin.models import TextModel
from contact_form_plugin.forms import ContactForm
from activity_cards_plugin.models import ActivityCard

from cms.models import Page


@plugin_pool.register_plugin
class ContactBarPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Contact Bar")
    render_template = "contact_bar_plugin/contact_bar.html"
    cache = False
    allow_children = True
    child_classes = ['ContactPlugin']

    def render(self, context, instance, placeholder):
        context = super(ContactBarPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class ContactPlugin(CMSPluginBase):
    # model = models.ContactList
    model = Contact
    name = _("Contact")
    render_template = "contact_bar_plugin/contact.html"
    cache = False
    require_parent = True
    parent_classes = ['ContactBarPlugin']

    def render(self, context, instance, placeholder):
        context = super(ContactPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class PhotoCarouselPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Photo-Carousel")
    render_template = "photo_carousel_plugin/carousel.html"
    cache = False
    allow_children = True
    child_classes = ['CarouselPhotoPlugin']

    def render(self, context, instance, placeholder):
        context = super(PhotoCarouselPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class CarouselPhotoPlugin(CMSPluginBase):
    model = CarouselPhoto
    name = _("Carousel Photo")
    render_template = "photo_carousel_plugin/photo.html"
    cache = False
    require_parent = True
    parent_classes = ['PhotoCarouselPlugin']

    def render(self, context, instance, placeholder):
        context = super(CarouselPhotoPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class TextBubblePlugin(CMSPluginBase):
    model = TextModel
    name = _("Text Bubble")
    render_template = "text_bubble_plugin/text_bubble.html"
    # cache = False

    def render(self, context, instance, placeholder):
        context = super(TextBubblePlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class ContactFormPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Contact Form")
    render_template = "contact_form_plugin/contact_form.html"
    # cache = False

    def render(self, context, instance, placeholder):
        context = super(ContactFormPlugin, self).render(context, instance, placeholder)
        context.update({
            'form': ContactForm()
        })
        context['contact_form'] = ContactForm()
        return context


@plugin_pool.register_plugin
class CardsContainerPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Activity Card Container")
    render_template = "activity_cards_plugin/card_container.html"
    cache = False
    allow_children = True
    child_classes = ['ActivityCardPlugin']

    def render(self, context, instance, placeholder):
        context = super(CardsContainerPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class ActivityCardPlugin(CMSPluginBase):
    model = ActivityCard
    name = _("Activity Card")
    render_template = "activity_cards_plugin/activity_card.html"
    cache = False
    require_parent = True
    parent_classes = ['CardsContainerPlugin']

    def render(self, context, instance, placeholder):
        context = super(ActivityCardPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class NavbarPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Navigation Bar")
    render_template = "navbar_plugin/navbar.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(NavbarPlugin, self).render(context, instance, placeholder)

        # categories = []
        # sorted_pages = {}
        # for page in Page.objects.all():
        #     # if page.category not in categories:
        #     #     categories[page.category] = []
        #     data = {'name': page.name, 'link': page.link}
        #     sorted_pages[page.category].append(data)
        #
        # context.update({
        #     'categories': categories,
        #     'sorted_pages': sorted_pages,
        # })
        return context

