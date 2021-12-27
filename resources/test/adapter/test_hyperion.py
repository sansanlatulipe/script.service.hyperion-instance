from resources.test.testmod import unittest
from resources.test.testmod import mock
from resources.lib.infra import hyperion


class HttpShould(unittest.TestCase):
    @mock.patch('resources.lib.infra.pymod.HTTPConnection')
    def setUp(self, connection):
        self.connection = connection
        self.http = hyperion.Http(connection)

    def test_send_a_simple_request_when_call_with_no_parameter(self):
        self.connection.request = mock.Mock(return_value=None)

        self.http.call('serverinfo')

        self.connection.request.assert_called_once_with(
            'POST',
            '/json-rpc',
            '{"command":"serverinfo"}',
            {}
        )

    def test_response_is_parsed_when_request_is_sucessful(self):
        self.connection.getresponse = self._buildMockResponse(True)

        response = self.http.call('serverinfo')

        self.connection.getresponse.read.decode.assert_called_once()
        self.assertEqual({'success': True}, response)

    def test_error_is_thrown_when_request_is_not_sucessful(self):
        self.connection.getresponse = self._buildMockResponse(False)

        with self.assertRaises(IOError):
            response = self.http.call('serverinfo')

    def test_send_a_request_with_data_when_call_with_parameters(self):
        self.connection.request = mock.Mock(return_value=None)

        self.http.call('instance', {
            'subcommand': 'startInstance',
            'instance': 1
        })

        self.connection.request.assert_called_once_with(
            'POST',
            '/json-rpc',
            '{"command":"instance","subcommand":"startInstance","instance":1}',
            {}
        )

    def _buildMockResponse(self, success):
        response = mock.Mock()
        response.read = mock.Mock()
        response.read.decode = mock.Mock(return_value='{"success": {}}'.format(succes))
        return response
