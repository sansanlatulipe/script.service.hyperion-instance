from resources.lib.infra.xbmcmod import Player


class MyPlayer(Player):
    def setLedManager(self, ledManager):
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
