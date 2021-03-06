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

class test_19393(GaiaTestCase):
    _Description = "[BASIC][EVERYTHING.ME] Install and launch an everything.me app - verify the everything.me app launches successfully to the right web content."
    
    _GROUP_NAME  = "Games"
    _APP_NAME    = "Tetris"
    _APP_FRAME   = ("src", "https://aduros.com/block-dream")
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        
        self.UTILS      = UTILS(self)
        self.Settings   = AppSettings(self)
        self.EME        = AppEverythingMe(self)
        
        
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Make sure 'things' are as we expect them to be first.
        #
        self.UTILS.getNetworkConnection()
        
        #
        # Make sure our app isn't installed already.
        #
        self.UTILS.uninstallApp(self._APP_NAME)
            
        #
        # Don't prompt me for geolocation (this was broken recently in Gaia, so 'try' it).
        #
        try:
            self.apps.set_permission('Homescreen', 'geolocation', 'deny')
        except:
            self.UTILS.logComment("(Just FYI) Unable to automatically set Homescreen geolocation permission.")

        #
        # Launch the 'everything.me' app.
        #
        self.EME.launch()
        
        #
        # Pick a group.
        #
        self.UTILS.TEST(self.EME.pickGroup(self._GROUP_NAME),
                        "Group '" + self._GROUP_NAME + "' exists in EverythingME.",
                        True)

        #
        # Add the app to the homescreen.
        #
        self.UTILS.TEST(self.EME.addAppToHomescreen(self._APP_NAME),
                        "Application '" + self._APP_NAME + "' is added to the homescreen.",
                        True)
        
        #
        # Go back to the homescreen and check it's installed.
        #
        self.UTILS.TEST(self.UTILS.launchAppViaHomescreen(self._APP_NAME), 
                        self._APP_NAME + " is installed.", True)
        
        #
        # Give it 10 seconds to start up, switch to the frame for it and grab a screenshot.
        #
        time.sleep(10)
        self.marionette.switch_to_frame()
        self.UTILS.switchToFrame(*self._APP_FRAME)
        x = self.UTILS.screenShot("19393_" + self._APP_NAME)
        self.UTILS.logComment("NOTE: Please check the game screenshot in " + x)
