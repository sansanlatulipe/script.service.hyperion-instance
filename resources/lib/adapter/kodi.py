from resources.lib.infra.xbmcmod import Monitor
from resources.lib.infra.xbmcmod import Player


class MyMonitor(Monitor):
    pass


class MyPlayer(Player):
    def __init__(self, ledManager):
        Player.__init__(self)
        self.ledManager = ledManager

    def onPlayBackStarted(self):
        if self.isPlayingVideo():
            self.ledManager.on()

    def onPlayBackResumed(self):
        self.onPlayBackStarted()

    def onPlayBackStopped(self):
        self.ledManager.off()

    def onPlayBackEnded(self):
        self.onPlayBackStopped()

    def onPlayBackPaused(self):
        self.onPlayBackStopped()
