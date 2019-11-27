from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

from cms.models import Page

#
# @menu_pool.register_menu
# class ActivitiesMenu(Menu):
#     def get_nodes(self, request):
#         nodes = []
#         n1 = NavigationNode(_('Activities'), "/", 1)
#         nodes.append(n1)
#         return nodes
#


@menu_pool.register_menu
class OtherMenu(CMSAttachMenu):
    # Menu Name (shows in dropdown)
    name = _("Category Menu")
    
    def get_nodes(self, request):
        nodes = []
        # list all pages
        all_pages = Page.objects.all()
        categories = {}
        
        for page in all_pages:
            if page.category not in categories.keys():
                categories[page.category] = []
            categories[page.category].append((page.name, page.link))
        
        for cat in categories:
            # create dropdown item for each category
            # populate with links for pages in category
        
        return nodes
    
    
# menu_pool.register_menu(OtherMenu)
