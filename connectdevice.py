#! /usr/bin/env python

import sys
import os

    
try:
    sys.path.insert(0, os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass
   
from com.dtmilano.android.viewclient import ViewClient
from com.dtmilano.android.viewclient import View

devices = *ViewClient.connectToDeviceOrExit()
print devices
#vc = ViewClient(*ViewClient.connectToDeviceOrExit())


