import json
from resources.lib.infra import pymod


class Http:
    def __init__(self, connection, token):
        self.connection = connection
        self.headers = {'Authorization': 'token {}'.format(token)} if token else {}

    def call(self, command, data=None):
        body = self._formatBody(command, data)
        self._prepareRequest(body)
        return self._decodeResponse()

    def _formatBody(self, command, data):
        body = {'command': command}
        if isinstance(data, dict):
            body.update(data)

        return json.dumps(body)

    def _prepareRequest(self, body):
        self.connection.request(
            'POST',
            '/json-rpc',
            body,
            self.headers
        )

    def _decodeResponse(self):
        response = json.loads(self.connection.getresponse().read().decode())
        if not response.get('succes'):
            raise IOError(response.get('error'))
        return response
