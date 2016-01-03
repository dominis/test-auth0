#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import threading
import xbmc
import xbmcaddon
import requests

__addon__         = xbmcaddon.Addon()
__cwd__           = __addon__.getAddonInfo('path')
__icon_path__     = __addon__.getAddonInfo("icon")
__icon__          = xbmc.translatePath(__icon_path__).decode('utf-8')
__scriptname__    = __addon__.getAddonInfo('name')
__version__       = __addon__.getAddonInfo('version')
__language__      = __addon__.getLocalizedString
__resource_path__ = os.path.join(__cwd__, 'resources', 'lib')
__resource__      = xbmc.translatePath(__resource_path__).decode('utf-8')


class Player(xbmc.Player):

    def __init__(self):
        xbmc.Player.__init__(self)
        self._total_time = 999999
        self._last_pos = 0
        self._tracker = None
        self._playback_lock = threading.Event()

    def _trackPosition(self):
        while self._playback_lock.isSet() and not xbmc.abortRequested:
            try:
                self._last_pos = self.getTime()
            except:
                self._playback_lock.clear()
            xbmc.sleep(250)

    def _setUp(self):
        self._playback_lock.set()
        self._tracker = threading.Thread(target=self._trackPosition)

    def _tearDown(self):
        if hasattr(self, '_playback_lock'):
            self._playback_lock.clear()
        if not hasattr(self, '_tracker'):
            return
        if self._tracker is None:
            return
        if self._tracker.isAlive():
            self._tracker.join()
        self._tracker = None

    def onPlayBackStarted(self):
        self._setUp()
        self._total_time = self.getTotalTime()
        self._tracker.start()

    def onPlayBackStopped(self):
        url = 'https://webtask.it.auth0.com/api/run/wt-dominis-haxor_hu-0/dummy?webtask_no_cache=1&data=%s' % self._last_pos

        self._tearDown()
        actual_percent = (self._last_pos/self._total_time)*100

        if actual_percent < 90:
            r = requests.get(url)

        log(actual_percent)
        log(r.text)


def log(msg):
    xbmc.log("### [%s] - %s" % (__scriptname__, str(msg).encode('utf-8'), ),
             level=xbmc.LOGDEBUG)


if __name__ == "__main__":
    player = Player()

    while not xbmc.abortRequested:
        xbmc.sleep(100)

    player._tearDown()
    sys.exit(0)
