'''

Created on March 2018
Framework Conceived by : Venkata Madduri
@author: Venkata Madduri
Refactoring of method names is finished

'''

from robot.api.deco import keyword
from AllNavigations.gmail_bo import GmailBOClass



class WebApplicationKeywords():
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        '''
        this is a class constructor
        '''

    @keyword('Get Verification code')
    def get_verification_code(self, gmail_uname, gmail_pwrd, xpected_uname):
        gpo = GmailBOClass()
        vercode = gpo.get_verification_code_from_gmail(gmail_uname, gmail_pwrd, xpected_uname)
        return vercode

    @keyword('Get Gmail save attachment content')
    def get_gmail_save_attachment_content(self, target_filepath):
        gpo = GmailBOClass()
        gpo.save_attachment_content(target_filepath)

    @keyword('Gmail Login')
    def gmail_login(self, gmail_uname, gmail_pwrd, xpected_uname):
        gpo = GmailBOClass()
        drvr = gpo.log_into_gmail(gmail_uname, gmail_pwrd)
        return drvr
