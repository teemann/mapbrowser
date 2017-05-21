import logging

from pyplanet.apps.config import AppConfig
from pyplanet.contrib.command import Command
from pyplanet.contrib.permission import PermissionManager
from pyplanet.contrib.command import CommandManager
from pyplanet.contrib.chat import ChatManager
from pyplanet.contrib.chat.query import ChatQuery
from .view import BrowserView

"""

"""
class MapBrowser(AppConfig):
    game_dependencies = ['trackmania']
    app_dependencies = ['core.maniaplanet', 'core.trackmania']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    async def on_start(self):
        await self.instance.permission_manager.register('localmaps', 'Shows a file browser to browse the local files', app=self, min_level=3)

        await self.instance.command_manager.register(
            Command(command='localmaps', target=self.show_browser, perms='mapbrowser:localmaps', admin=True)
        )

    async def show_browser(self, player, data, **kwargs):
        view = BrowserView(self, player)
        await view.set_dir('')