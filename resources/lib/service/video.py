class Monitor:
    def __init__(self, kodiMonitor, kodiPlayer):
        self.monitor = kodiMonitor
        self.player = kodiPlayer

    def run(self):
        while not self.monitor.abortRequested():
            self.monitor.waitForAbort(60)
