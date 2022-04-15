from resources.lib.infra.xbmcmod import Dialog
from resources.lib.util.di import Container


class Launcher:
    def __init__(self):
        self.container = Container()

    def switch(self):
        try:
            self.container.get('led.manager').switch()
        except IOError as error:
            Dialog().ok(self.container.get('addon').getAddonInfo('name'), str(error))

    def selectInstance(self):
        try:
            selectedInstance = Dialog().select(
                self.container.get('addon').getLocalizedString(30200).encode('utf-8'),
                self.container.get('led.manager').listInstances()
            )
            self.container.get('led.manager').selectInstance(selectedInstance)
        except IOError as error:
            Dialog().ok(self.container.get('addon').getAddonInfo('name'), str(error))

    def monitor(self):
        self.container.get('video.monitor').run()
