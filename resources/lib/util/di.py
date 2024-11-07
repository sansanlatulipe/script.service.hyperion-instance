from http.client import HTTPConnection
import xbmc
import xbmcaddon
from resources.lib.adapter import hyperion as hyperionAdapter
from resources.lib.adapter import kodi
from resources.lib.adapter import settings
from resources.lib.infra import hyperion as hyperionInfra
from resources.lib.service import led
from resources.lib.service import video
from resources.lib.util import logger


class Container:
    def __init__(self):
        self.singletons = {}

    def get(self, service):
        if service not in self.singletons:
            initializer = '_init' + service.title().replace('.', '')
            self.singletons[service] = getattr(self, initializer)()
        return self.singletons[service]

    def _initAddon(self):
        return xbmcaddon.Addon()

    def _initHyperionHttp(self):
        return hyperionInfra.Http(
            self.get('logger'),
            HTTPConnection(
                self.get('settings').getHyperionIp(),
                self.get('settings').getHyperionPort()
            ),
            self.get('settings').getHyperionToken()
        )

    def _initHyperionInstance(self):
        return hyperionAdapter.Instance(
            self.get('hyperion.http'),
            self.get('settings')
        )

    def _initKodiMonitor(self):
        return xbmc.Monitor()

    def _initKodiPlayer(self):
        player = kodi.MyPlayer()
        player.setLedManager(self.get('led.manager'))
        return player

    def _initLedManager(self):
        return led.Manager(
            self.get('logger'),
            self.get('hyperion.instance')
        )

    def _initLogger(self):
        return logger.Logger(
            self.get('addon')
        )

    def _initSettings(self):
        return settings.Settings(
            self.get('addon')
        )

    def _initVideoMonitor(self):
        return video.Monitor(
            self.get('kodi.monitor'),
            self.get('kodi.player')
        )
