from resources.lib.infra.xbmcmod import Player


class MyPlayer(Player):
    def __init__(self):
        self.ledManager = None
        Player.__init__(self)

    def setLedManager(self, ledManager):
        self.ledManager = ledManager

    def onPlayBackStarted(self):
        if self.isPlayingVideo():
            try:
                self.ledManager.on()
            except IOError:
                pass

    def onPlayBackResumed(self):
        self.onPlayBackStarted()

    def onAVStarted(self):
        self.onPlayBackStarted()

    def onPlayBackStopped(self):
        try:
            self.ledManager.off()
        except IOError:
            pass

    def onPlayBackEnded(self):
        self.onPlayBackStopped()

    def onPlayBackPaused(self):
        self.onPlayBackStopped()
