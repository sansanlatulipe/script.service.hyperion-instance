import unittest
from unittest import mock
from resources.lib.adapter import kodi


class MyPlayerShould(unittest.TestCase):
    @mock.patch('resources.lib.service.led.Manager')
    def setUp(self, ledManager):
        self.ledManager = ledManager
        self.player = kodi.MyPlayer()
        self.player.setLedManager(ledManager)

    def test_turn_led_on_when_start_playing_video(self):
        self.player.isPlayingVideo = mock.Mock(return_value=True)
        self.ledManager.on = mock.Mock(return_value=None)

        self.player.onPlayBackStarted()
        self.player.onPlayBackResumed()
        self.player.onAVStarted()

        self.assertEqual(3, self.ledManager.on.call_count)

    def test_not_turn_led_on_when_start_playing_music(self):
        self.player.isPlayingVideo = mock.Mock(return_value=False)
        self.ledManager.on = mock.Mock(return_value=None)

        self.player.onPlayBackStarted()
        self.player.onPlayBackResumed()
        self.player.onAVStarted()

        self.ledManager.on.assert_not_called()

    def test_turn_led_off_when_stop_playing(self):
        self.ledManager.off = mock.Mock(return_value=None)

        self.player.onPlayBackStopped()
        self.player.onPlayBackEnded()
        self.player.onPlayBackPaused()

        self.assertEqual(3, self.ledManager.off.call_count)

    def test_ignore_manager_error_when_turning_instance_on(self):
        self.player.isPlayingVideo = mock.Mock(return_value=True)
        self.ledManager.on = mock.Mock(side_effect=IOError())

        self.player.onPlayBackStarted()
        self.player.onPlayBackResumed()
        self.player.onAVStarted()

        self.assertEqual(3, self.ledManager.on.call_count)

    def test_ignore_manager_error_when_turning_instance_off(self):
        self.ledManager.off = mock.Mock(side_effect=IOError())

        self.player.onPlayBackStopped()
        self.player.onPlayBackEnded()
        self.player.onPlayBackPaused()

        self.assertEqual(3, self.ledManager.off.call_count)
