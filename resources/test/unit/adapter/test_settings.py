import unittest
from unittest import mock
from resources.lib.adapter import settings


class SettingsShould(unittest.TestCase):
    @mock.patch('xbmcaddon.Addon')
    def setUp(self, addon):
        self.addon = addon
        self.settings = settings.Settings(addon)

    def test_get_addon_id_from_addon_info(self):
        expectedAddonId = 'hyperion-instance'
        self.addon.getAddonInfo = mock.Mock(return_value=expectedAddonId)

        addonId = self.settings.getAddonId()

        self.addon.getAddonInfo.assert_called_once_with('id')
        self.assertEqual(expectedAddonId, addonId)

    def test_get_hyperion_ip_from_addon_settings(self):
        expectedSetting = '1.2.3.4'
        self.addon.getSetting = mock.Mock(return_value=expectedSetting)

        setting = self.settings.getHyperionIp()

        self.addon.getSetting.assert_called_once_with('hyperion_ip')
        self.assertEqual(expectedSetting, setting)

    def test_get_hyperion_port_from_addon_settings(self):
        expectedSetting = 1234
        self.addon.getSettingInt = mock.Mock(return_value=expectedSetting)

        setting = self.settings.getHyperionPort()

        self.addon.getSettingInt.assert_called_once_with('hyperion_port')
        self.assertEqual(expectedSetting, setting)

    def test_get_hyperion_token_from_addon_settings(self):
        expectedSetting = 'a214b0-232c-a23-35236ce'
        self.addon.getSetting = mock.Mock(return_value=expectedSetting)

        setting = self.settings.getHyperionToken()

        self.addon.getSetting.assert_called_once_with('hyperion_token')
        self.assertEqual(expectedSetting, setting)

    def test_get_hyperion_instance_from_addon_settings(self):
        expectedSetting = 1
        self.addon.getSettingInt = mock.Mock(return_value=expectedSetting)

        setting = self.settings.getHyperionInstance()

        self.addon.getSettingInt.assert_called_once_with('hyperion_instance')
        self.assertEqual(expectedSetting, setting)

    def test_set_hyperion_instance_from_addon_settings(self):
        expectedSetting = 1
        self.addon.setSettingInt = mock.Mock()

        self.settings.setHyperionInstance(expectedSetting)

        self.addon.setSettingInt.assert_called_once_with('hyperion_instance', expectedSetting)
