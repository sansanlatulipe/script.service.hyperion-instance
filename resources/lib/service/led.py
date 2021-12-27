class Controller:
    def __init__(self, hyperionInstance):
        self.instance = hyperionInstance

    def on(self):
        self.instance.on()

    def off(self):
        self.instance.off()

    def switch(self):
        if self.instance.isOn():
            self.off()
        else:
            self.on()
