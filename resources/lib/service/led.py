from resources.lib.util import log


class Manager:
    def __init__(self, hyperionInstance):
        self.instance = hyperionInstance

    def listInstances(self):
        return list(map(
            lambda instance: instance.get('friendly_name'),
            self.instance.list()
        ))

    def selectInstance(self, instanceNum):
        self.instance.select(instanceNum)

    def on(self):
        log.info('Turning Hyperion managed instance on')
        self.instance.on()

    def off(self):
        log.info('Turning Hyperion managed instance off')
        self.instance.off()

    def switch(self):
        log.info('Manually switching Hyperion managed instance')
        if self.instance.isOn():
            self.off()
        else:
            self.on()
