#
# Imports which are standard for all test cases.
#
import sys
sys.path.insert(1, "./")
from gaiatest   import GaiaTestCase
from OWDTestToolkit import *

#
# Imports particular to this test case.
#
#from datetime 
import datetime, time   

class test_19325(GaiaTestCase):
    _Description = "(BLOCKED BY BUG 867987) [CLOCK] Alarm- Delete an alarm."

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.clock      = AppClock(self)
        self.settings   = AppSettings(self)
                
        #
        #
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
    
        #
        # Set the volume to be low (no need to wake up the office! ;o)
        #
        self.settings.setAlarmVolume(1)

        #        
        # Make sure the date and timezone are correct before setting alarms.
        #

        #
        # Launch clock app.
        #
        self.clock.launch()
        
        #
        # Delete all previous alarms.
        #
        #
        self.clock.deleteAllAlarms() 

        #
        # Create an alarm that is 2 minutes in the future.
        #
        # (Make sure we're not about to do this at the end of a minute or an hour.)
        #
        now_mins = time.strftime("%M", time.gmtime())
        diff_m   = 60 - int(now_mins)
        if diff_m <= 1:
            time.sleep(60)
        
        now_secs = time.strftime("%S", time.gmtime())
        diff_s   = 60 - int(now_secs)
        if diff_s <= 15:
            time.sleep(diff_s)


        t = datetime.datetime.now() + datetime.timedelta(minutes=2)
        
        _hour   = t.hour
        _minute = t.minute
        _title  = "Test alarm"

        self.clock.createAlarm(_hour, _minute, _title)

        #
        # Restart the Clock app.
        #
        self.clock.launch()
        
        #
        # Delete the alarm.
        #
        self.clock.deleteAllAlarms()
