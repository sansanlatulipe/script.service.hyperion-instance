from resources.test.testmod import unittest
from resources.test.testmod import mock
from resources.lib.adapter import hyperion


class InstanceShould(unittest.TestCase):
    @mock.patch('resources.lib.infra.hyperion.Http')
    @mock.patch('resources.lib.adapter.settings.Settings')
    def setUp(self, http, settings):
        self.http = http
        self.settings = settings
        self.instance = hyperion.Instance(http, settings)

        self.settings.getHyperionInstance = mock.Mock(return_value=1)

    def test_list_instances_from_hyperion_server_info(self):
        self.http.call = mock.Mock(return_value=self._buildServerInfo())

        instances = self.instance.list()

        self.http.call.assert_called_once_with('serverinfo')
        self.assertEqual(self._buildInstances(1, True), instances)

    def test_update_settings_with_instance_id_when_a_new_managed_instance_is_selected(self):
        self.http.call = mock.Mock(return_value=self._buildServerInfo(managedInstance=3))
        self.settings.setHyperionInstance = mock.Mock()

        self.instance.select(0)

        self.http.call.assert_called_once_with('serverinfo')
        self.settings.setHyperionInstance.assert_called_once_with(3)

    def test_be_on_when_managed_instance_is_running(self):
        self.http.call = mock.Mock(return_value=self._buildServerInfo())

        isOn = self.instance.isOn()

        self.http.call.assert_called_once_with('serverinfo')
        self.assertTrue(isOn)

    def test_be_off_when_managed_instance_is_not_running(self):
        self.http.call = mock.Mock(return_value=self._buildServerInfo(isOn=False))

        isOn = self.instance.isOn()

        self.assertFalse(isOn)

    def test_be_off_when_managed_instance_does_not_exist(self):
        self.http.call = mock.Mock(return_value=self._buildServerInfo(managedInstance=3))

        isOn = self.instance.isOn()

        self.assertFalse(isOn)

    def test_start_managed_instance_when_turning_it_on(self):
        self.http.call = mock.Mock()

        self.instance.on()

        self.http.call.assert_called_once_with('instance', {
            'subcommand': 'startInstance', 'instance': 1
        })

    def test_stop_managed_instance_when_turning_it_off(self):
        self.http.call = mock.Mock()

        self.instance.off()

        self.http.call.assert_called_once_with('instance', {
            'subcommand': 'stopInstance', 'instance': 1
        })

    def _buildServerInfo(self, managedInstance=1, isOn=True):
        return {
            'success': True,
            'info': {
                'foo': ['bar'],
                'instance': [
                    {'instance': 0, 'running': False, 'friendly_name': 'My First LED Hardware instance'}
                ] + self._buildInstances(managedInstance, isOn)
            }
        }

    def _buildInstances(self, managedInstance, isOn):
        return [
            {'instance': managedInstance, 'running': isOn, 'friendly_name': 'Instance 1'},
            {'instance': 2, 'running': False, 'friendly_name': 'Instance 2'}
        ]
