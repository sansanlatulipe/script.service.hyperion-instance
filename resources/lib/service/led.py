class Manager:
    def __init__(self, logger, hyperionInstance):
        self.logger = logger
        self.instance = hyperionInstance

    def listInstances(self):
        return list(map(
            lambda instance: instance.get('friendly_name'),
            self.instance.list()
        ))

    def selectInstance(self, instanceNum):
        self.instance.select(instanceNum)

    def on(self):
        self.logger.info('Turning Hyperion managed instance on')
        self.instance.on()

    def off(self):
        self.logger.info('Turning Hyperion managed instance off')
        self.instance.off()

    def switch(self):
        self.logger.info('Manually switching Hyperion managed instance')
        if self.instance.isOn():
            self.off()
        else:
            self.on()
