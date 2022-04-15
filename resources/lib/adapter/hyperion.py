class Instance:
    def __init__(self, http, settings):
        self.http = http
        self.settings = settings

    def list(self):
        return [
            instance
            for instance in self.http.call('serverinfo').get('info').get('instance')
            if instance.get('instance') != 0
        ]

    def select(self, num):
        instances = self.list()
        self.settings.setHyperionInstance(instances[num].get('instance'))

    def isOn(self):
        for instance in self.list():
            if instance.get('instance') == self.settings.getHyperionInstance():
                return instance.get('running')
        return False

    def on(self):
        self.http.call('instance', {
            'subcommand': 'startInstance',
            'instance': self.settings.getHyperionInstance()
        })

    def off(self):
        self.http.call('instance', {
            'subcommand': 'stopInstance',
            'instance': self.settings.getHyperionInstance()
        })
