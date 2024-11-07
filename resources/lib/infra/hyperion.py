import json


class Http:
    def __init__(self, logger, connection, token):
        self.logger = logger
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
        if not response.get('success'):
            self.logger.warn('An error occurs while calling Hyperion API: ' + response.get('error'))
            raise IOError(response.get('error'))
        return response
