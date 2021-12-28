from resources.test.testmod import unittest
from resources.test.testmod import mock
from resources.lib.service import led


class ManagerShould(unittest.TestCase):
    @mock.patch('resources.lib.adapter.hyperion.Instance')
    def setUp(self, instance):
        self.instance = instance
        self.manager = led.Manager(instance)

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
