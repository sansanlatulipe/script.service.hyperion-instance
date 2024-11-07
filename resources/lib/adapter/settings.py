class Settings:
    def __init__(self, addon):
        self.addon = addon

    def getAddonId(self):
        return self.addon.getAddonInfo('id')

    def getHyperionIp(self):
        return self.addon.getSetting('hyperion_ip')

    def getHyperionPort(self):
        return self.addon.getSettingInt('hyperion_port')

    def getHyperionToken(self):
        return self.addon.getSetting('hyperion_token')

    def getHyperionInstance(self):
        return self.addon.getSettingInt('hyperion_instance')

    def setHyperionInstance(self, instance):
        self.addon.setSettingInt('hyperion_instance', int(instance))
