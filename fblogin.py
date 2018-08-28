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

screen_one = ViewClient(*ViewClient.connectToDeviceOrExit())
email = screen_one.findViewByIdOrRaise("m_login_email")
email.touch()
email.setText("x2012ato@stfx.ca")

screen_one = ViewClient(*ViewClient.connectToDeviceOrExit())
passwd = screen_one.findViewByIdOrRaise("m_login_password")
passwd.touch()
passwd.setText("aragon911119")

screen_one = ViewClient(*ViewClient.connectToDeviceOrExit())
loginbtn = screen_one.findViewByIdOrRaise("u_0_5")
loginbtn.touch()

time.sleep(5)

done = False
while done == False:
    try:
        screen_two = ViewClient(*ViewClient.connectToDeviceOrExit())
        continuebtn = screen_two.findViewByIdOrRaise("u_0_9")
        done = True
        continuebtn.touch()
    except ViewNotFoundException:
        print 'still loading'
        time.sleep(1)
        

        




