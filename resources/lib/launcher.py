from resources.lib.util.di import Container


class Launcher:
    def __init__(self):
        self.container = Container()

    def switch(self):
        self.container.get('led.manager').switch()

    def monitor(self):
        self.container.get('video.monitor').run()
