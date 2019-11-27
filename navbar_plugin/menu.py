from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _


class ActivitiesMenu(Menu):
    def get_nodes(self, request):
        nodes = []
        n1 = NavigationNode(_('Activities'), "/", 1)
        nodes.append(n1)
        return nodes
    
    
menu_pool.register_menu(ActivitiesMenu)
