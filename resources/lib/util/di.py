from resources.lib.adapter import hyperion as hyperionAdapter
from resources.lib.adapter import kodi
from resources.lib.adapter import settings
from resources.lib.infra import hyperion as hyperionInfra
from resources.lib.infra import pymod
from resources.lib.infra import xbmcmod
from resources.lib.service import led
from resources.lib.service import video


class Container:
    def __init__(self):
        self.singletons = {}
        self.settings = settings.Settings(self.get('addon'))

    def get(self, service):
        if service not in self.singletons:
            initializer = '_init' + service.title().replace('.', '')
            self.singletons[service] = getattr(self, initializer)()
        return self.singletons[service]

    def _initAddon(self):
        return xbmcmod.Addon()

    def _initLedManager(self):
        return led.Manager(
            self.get('hyperion.instance')
        )

    def _initVideoMonitor(self):
        return video.Monitor(
            self.get('kodi.monitor'),
            self.get('kodi.player')
        )

    def _initHyperionInstance(self):
        return hyperionAdapter.Instance(
            self.get('hyperion.http'),
            self.settings
        )

    def _initKodiMonitor(self):
        return xbmcmod.Monitor()

    def _initKodiPlayer(self):
        player = kodi.MyPlayer()
        player.setLedManager(self.get('led.manager'))
        return player

    def _initHyperionHttp(self):
        return hyperionInfra.Http(
            pymod.HTTPConnection(
                self.settings.getHyperionIp(),
                self.settings.getHyperionPort()
            ),
            self.settings.getHyperionToken()
        )
