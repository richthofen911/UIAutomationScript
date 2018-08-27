#! /usr/bin/env python

import sys
import os

    
try:
    sys.path.insert(0, os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass
   
from com.dtmilano.android.viewclient import ViewClient
from com.dtmilano.android.viewclient import View

#Hyprmediate AdColony "control-closeButton"
#Admob                "delay_close_button"

vc = ViewClient(*ViewClient.connectToDeviceOrExit())

vc.traverse()
