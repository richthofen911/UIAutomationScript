#! /usr/bin/env python

import sys
import os
import time

    
try:
    sys.path.insert(0, os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass
   
from com.dtmilano.android.viewclient import ViewClient
from com.dtmilano.android.viewclient import View
from com.dtmilano.android.viewclient import ViewNotFoundException

time.sleep(1)
ad_end_screen = ViewClient(*ViewClient.connectToDeviceOrExit())

ready_to_install = False
while ready_to_install == False:
    try:
        install_btn = ad_end_screen.findViewByIdOrRaise("GEC CTA Button")
        ready_to_install = True
        install_btn.touch()
    except ViewNotFoundException:
        print 'ad not ended'
        time.sleep(1)

time.sleep(2)

play_store_screen = ViewClient(*ViewClient.connectToDeviceOrExit())
play_store_install_btn = play_store_screen.findViewWithTextOrRaise("INSTALL")
play_store_install_btn.touch()

time.sleep(10)


ready_to_open = False
while ready_to_open == False:
    try:
        app_installed_screen = ViewClient(*ViewClient.connectToDeviceOrExit())
        open_btn = app_installed_screen.findViewWithTextOrRaise("OPEN")
        ready_to_open = True
        open_btn.touch()
    except ViewNotFoundException:
        print 'still installing'
        time.sleep(10)

#btn = vc.findViewByIdOrRaise("android:id/button1")
#btn = vc.findViewWithText("UNINSTALL")
#btn.touch()
