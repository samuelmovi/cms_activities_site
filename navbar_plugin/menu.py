from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

#
# @menu_pool.register_menu
# class ActivitiesMenu(Menu):
#     def get_nodes(self, request):
#         nodes = []
#         n1 = NavigationNode(_('Activities'), "/", 1)
#         nodes.append(n1)
#         return nodes
#
#
# # menu_pool.register_menu(ActivitiesMenu)
#
#
# @menu_pool.register_menu
# class OtherMenu(CMSAttachMenu):
#     # Menu Name (shows in dropdown)
#     name = _("Category Menu")
#
#     def get_nodes(self, request):
#         nodes = []
#         n1 = NavigationNode(_('Test1'), "/newpost1/", 1)
#         n2 = NavigationNode(_('Test2'), "/newpost2/", 2)
#         n3 = NavigationNode(_('Test3'), "/newpost3/", 3)
#         nodes.append(n1)
#         nodes.append(n2)
#         nodes.append(n3)
#         return nodes
#
#
# # menu_pool.register_menu(OtherMenu)

