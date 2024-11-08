import json
import unittest
from unittest import mock
from resources.lib.infra import hyperion


class HttpShould(unittest.TestCase):
    @mock.patch('http.client.HTTPConnection')
    @mock.patch('resources.lib.util.logger.Logger')
    def setUp(self, logger, connection):
        self.logger = logger
        self.connection = connection
        self.http = hyperion.Http(self.logger, self.connection, None)

    def test_send_a_post_request_with_the_wanted_command(self):
        self.connection.request = mock.Mock()
        self.connection.getresponse = mock.Mock(return_value=FakeResponse())

        self.http.call('serverinfo')

        self.connection.request.assert_called_once_with(
            'POST',
            '/json-rpc',
            '{"command": "serverinfo"}',
            {}
        )

    def test_send_a_post_request_with_the_additional_data(self):
        self.connection.request = mock.Mock()
        self.connection.getresponse = mock.Mock(return_value=FakeResponse())

        expectedBody = {'command': 'instance'}
        expectedBody.update({'subcommand': 'startInstance'})

        self.http.call('instance', {'subcommand': 'startInstance'})

        self.connection.request.assert_called_once_with(
            'POST',
            '/json-rpc',
            json.dumps(expectedBody),
            {}
        )

    def test_decode_response_as_dictionary_object_when_successful(self):
        self.connection.request = mock.Mock()
        self.connection.getresponse = mock.Mock(return_value=FakeResponse())

        response = self.http.call('serverinfo')

        self.connection.getresponse.assert_called_once()
        self.assertEqual({'success': True}, response)

    def test_raise_a_io_error_when_not_successul(self):
        self.connection.request = mock.Mock()
        self.connection.getresponse = mock.Mock(return_value=FakeResponse(False))

        with self.assertRaises(IOError) as context:
            self.http.call('serverinfo')

        self.assertEqual('bad request', str(context.exception))


class FakeResponse:
    def __init__(self, success=True):
        message = '{"success": true}' if success else '{"success": false, "error": "bad request"}'
        self.msg = message.encode()

    def read(self):
        return self.msg
