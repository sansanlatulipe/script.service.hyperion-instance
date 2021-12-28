from resources.lib.util.di import Container
from resources.lib.infra.xbmcmod import Dialog


class Launcher:
    def __init__(self):
        self.container = Container()

    def switch(self):
        try:
            self.container.get('led.manager').switch()
        except IOError as error:
            Dialog().ok('Hyperion instance switcher', str(error))

    def monitor(self):
        self.container.get('video.monitor').run()
