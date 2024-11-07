import xbmc


class Logger:
    def __init__(self, addon):
        self.addon = addon

    def debug(self, msg):
        self._log(msg, xbmc.LOGDEBUG)

    def info(self, msg):
        self._log(msg, xbmc.LOGINFO)

    def warn(self, msg):
        self._log(msg, xbmc.LOGWARNING)

    def error(self, msg):
        self._log(msg, xbmc.LOGERROR)

    def _log(self, msg, loglvl):
        xbmc.log('{}: {}'.format(self.addon.getAddonInfo('id'), msg), loglvl)
