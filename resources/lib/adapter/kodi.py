from resources.lib.infra.xbmcmod import Monitor
from resources.lib.infra.xbmcmod import Player


class MyMonitor(Monitor):
    pass


class MyPlayer(Player):
    def __init__(self, ledController):
        Player.__init__(self)
        self.ledController = ledController

    def onPlayBackStarted(self):
        if self.isPlayingVideo():
            self.ledController.on()

    def onPlayBackResumed(self):
        self.onPlayBackStarted()

    def onPlayBackStopped(self):
        self.ledController.off()

    def onPlayBackEnded(self):
        self.onPlayBackStopped()

    def onPlayBackPaused(self):
        self.onPlayBackStopped()
