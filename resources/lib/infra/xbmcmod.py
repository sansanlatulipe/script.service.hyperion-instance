# pylint: disable=unused-import
# flake8: noqa

try:
    from xbmc import log, LOGDEBUG, LOGINFO, LOGWARNING, LOGERROR
    from xbmc import Monitor, Player
    from xbmcaddon import Addon
    from xbmcgui import Dialog
except ImportError:
    LOGDEBUG = 'DEBUG'
    LOGINFO = 'INFO'
    LOGWARNING = 'WARNING'
    LOGERROR = 'ERROR'

    def log(msg, lvl):
        print(lvl, msg)


    class Monitor:
        def __init__(self):
            self.requests = 0

        def waitForAbort(self, timeout=0):
            pass

        def abortRequested(self):
            self.requests += 1
            return self.requests > 1


    class Player:
        def __init__(self):
            self.mode = None

        def isPlayingVideo(self):
            return self.mode == 'video'

        def setPlayingMode(self, mode):
            self.mode = mode


    class Addon:
        def __init__(self):
            self.settings = {
                'hyperion_ip': '127.0.0.1',
                'hyperion_port': '8090',
                'hyperion_token': None,
                'hyperion_instance': '1'
            }

        def getAddonInfo(self, key):
            if key == 'id':
                return 'addon.fake'
            if key == 'name':
                return 'Fake add-on'
            if key == 'path':
                return '.'
            return None

        def getSetting(self, key):
            return self.settings.get(key)

        def getLocalizedString(self, labelId):
            return 'Message {}'.format(labelId)


    class Dialog:
        def ok(self, heading, text):
            print('{} > {}'.format(heading, text))
