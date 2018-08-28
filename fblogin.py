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

screen_one = ViewClient(*ViewClient.connectToDeviceOrExit())

email = screen_one.findViewByIdOrRaise("m_login_email")
passwd = screen_one.findViewByIdOrRaise("m_login_password")
loginbtn = screen_one.findViewByIdOrRaise("u_0_5")

email.setText("x2012ato@stfx.ca")
passwd.setText("aragon911119")
loginbtn.touch()

time.sleep(5)

screen_two = ViewClient(*ViewClient.connectToDeviceOrExit())
continuebtn = screen_two.findViewByIdOrRaise("u_0_9")
continuebtn.touch()


