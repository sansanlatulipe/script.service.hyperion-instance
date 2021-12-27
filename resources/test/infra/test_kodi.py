from resources.test.testmod import unittest
from resources.test.testmod import mock
from resources.lib.adapter import kodi


class MyMonitorShould(unittest.TestCase):
    def setUp(self):
        self.monitor = kodi.MyMonitor()

    def test_initialize_service(self):
        pass


class MyPlayerShould(unittest.TestCase):
    @mock.patch('resources.lib.service.led.Controller')
    def setUp(self, ledController):
        self.ledController = ledController
        self.player = kodi.MyPlayer(ledController)

    def test_turn_led_on_when_start_playing_video(self):
        self.ledController.on = mock.Mock(return_value=None)
        self.player.setPlayingMode('video')

        self.player.onPlayBackStarted()
        self.player.onPlayBackResumed()

        self.assertEqual(2, self.ledController.on.call_count)

    def test_not_turn_led_on_when_start_playing_music(self):
        self.ledController.on = mock.Mock(return_value=None)
        self.player.setPlayingMode('music')

        self.player.onPlayBackStarted()
        self.player.onPlayBackResumed()

        self.ledController.on.assert_not_called()

    def test_turn_led_off_when_stop_playing(self):
        self.ledController.off = mock.Mock(return_value=None)

        self.player.onPlayBackStopped()
        self.player.onPlayBackEnded()
        self.player.onPlayBackPaused()

        self.assertEqual(3, self.ledController.off.call_count)
