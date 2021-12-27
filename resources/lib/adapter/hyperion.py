class Instance:
    def __init__(self, http, controlledInstance):
        self.http = http
        self.controlledInstance = controlledInstance

    def list(self):
        return self.http.call('serverinfo').get('info').get('instance')

    def isOn(self):
        for instance in self.list():
            if instance.get('instance') == self.controlledInstance:
                return instance.get('running')
        return False

    def on(self):
        self.http.call('instance', {
            'subcommand': 'startInstance',
            'instance': self.controlledInstance
        })

    def off(self):
        self.http.call('instance', {
            'subcommand': 'stopInstance',
            'instance': self.controlledInstance
        })