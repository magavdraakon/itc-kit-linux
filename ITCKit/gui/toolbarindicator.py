__author__ = "Kristo Koert"
#Dependency: gir1.2-appindicator3

from gi.repository import Gtk, Gdk

try:
    from gi.repository import AppIndicator3 as AppIndicator
except ImportError:
    from gi.repository import AppIndicator

from ITCKit.core.notificationHandler import NotificationHandler
from ITCKit.gui.menus import MainMenu


Gdk.threads_init()


class ToolbarIndicator():

    _tracked_time = ''

    def __init__(self):
        import os
        icon_path = os.path.dirname(os.path.abspath(__file__)) + "/icon/Icon4.png"
        self.indc = AppIndicator.Indicator.new("app-doc-menu", icon_path,
                                               AppIndicator.IndicatorCategory.APPLICATION_STATUS)
        self.indc.set_status(AppIndicator.IndicatorStatus.ACTIVE)
        self.indc.set_attention_icon("indicator-messages-new")

        self.main_menu = MainMenu()
        self.indc.set_menu(self.main_menu)

        self._notification_handler = NotificationHandler(self.indc, self.main_menu.notification_display_widget)
        self._notification_handler.start()

    def set_notification_icon(self):
        #ToDo implement set_notification_icon
        pass


def activate_toolbar():
    gui = ToolbarIndicator()
    Gdk.threads_enter()
    Gtk.main()
    Gdk.threads_leave()

if __name__ == "__main__":
    activate_toolbar()