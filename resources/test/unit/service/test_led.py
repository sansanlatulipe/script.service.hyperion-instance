import unittest
from unittest import mock
from resources.lib.service import led


class ManagerShould(unittest.TestCase):
    @mock.patch('resources.lib.adapter.hyperion.Instance')
    @mock.patch('resources.lib.util.logger.Logger')
    def setUp(self, logger, instance):
        self.logger = logger
        self.instance = instance
        self.manager = led.Manager(self.logger, self.instance)

    def test_retrieve_available_instance_when_listing_them_from_hyperion(self):
        expectedInstances = ['Instance 1', 'Instance 2']
        self.instance.list = mock.Mock(return_value=[
            {'instance': 1, 'friendly_name': expectedInstances[0]},
            {'instance': 2, 'friendly_name': expectedInstances[1]}
        ])

        actualInstances = self.manager.listInstances()

        self.instance.list.assert_called_once()
        self.assertEqual(expectedInstances, actualInstances)

    def test_change_managed_instance_when_(self):
        self.instance.select = mock.Mock()

        self.manager.selectInstance(0)

        self.instance.select.assert_called_once_with(0)

    def test_turn_managed_instance_on_when_asked(self):
        self.instance.on = mock.Mock()

        self.manager.on()

        self.instance.on.assert_called_once()

    def test_turn_managed_instance_off_when_asked(self):
        self.instance.off = mock.Mock()

        self.manager.off()

        self.instance.off.assert_called_once()

    def test_switch_managed_instance_off_when_it_was_on(self):
        self.instance.isOn = mock.Mock(return_value=True)
        self.instance.off = mock.Mock()

        self.manager.switch()

        self.instance.isOn.assert_called_once()
        self.instance.off.assert_called_once()

    def test_switch_managed_instance_on_when_it_was_off(self):
        self.instance.isOn = mock.Mock(return_value=False)
        self.instance.on = mock.Mock()

        self.manager.switch()

        self.instance.isOn.assert_called_once()
        self.instance.on.assert_called_once()
