class Instance:
    def __init__(self, http, managedInstance):
        self.http = http
        self.managedInstance = managedInstance

    def list(self):
        return self.http.call('serverinfo').get('info').get('instance')

    def isOn(self):
        for instance in self.list():
            if instance.get('instance') == self.managedInstance:
                return instance.get('running')
        return False

    def on(self):
        self.http.call('instance', {
            'subcommand': 'startInstance',
            'instance': self.managedInstance
        })

    def off(self):
        self.http.call('instance', {
            'subcommand': 'stopInstance',
            'instance': self.managedInstance
        })
