import unittest
from unittest import mock
from resources.lib.service import video


class MonitorShould(unittest.TestCase):
    @mock.patch('xbmc.Monitor')
    @mock.patch('resources.lib.adapter.kodi.MyPlayer')
    def setUp(self, kodiMonitor, kodiPlayer):
        self.kodiMonitor = kodiMonitor
        self.kodiPlayer = kodiPlayer
        self.monitor = video.Monitor(kodiMonitor, kodiPlayer)

    def test_run_while_no_abort_is_requested(self):
        self.kodiMonitor.abortRequested = mock.Mock(side_effect=[False, True])
        self.kodiMonitor.waitForAbort = mock.Mock()

        self.monitor.run()

        self.kodiMonitor.waitForAbort.assert_called_once_with(60)
        self.assertEqual(2, self.kodiMonitor.abortRequested.call_count)
