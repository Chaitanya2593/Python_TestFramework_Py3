'''

Created on March 2018
Framework Conceived by : Venkata
@author: Venkata

'''

from selenium.webdriver.common.keys import Keys
from ActionsAll.common_actions import CommonActionsClass
from pageObjectsAll.gmailloginpage_po import GmailLoginPageObjectsClass
from Utilities.common_utilities import CommonUtilsClass
from commonVariables import master_key
import time
import re

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GmailLoginPageActionClass():

    def __init__(self, driver):
        '''
        this is a constructor of class
        :param driver:
        '''
        self.driver = driver

    def login_automation_gmail_account(self, user_name, gmail_pwrd):
        '''
        Gmail when u want to validate in Standard View
        :param user_name:
        :param gmail_pwrd:
        :return:
        '''
        gmail_po = GmailLoginPageObjectsClass(self.driver)
        ca = CommonActionsClass(self.driver)
        common_utils = CommonUtilsClass()
        email_textbox_elmnt = gmail_po.email_text_box_loc()
        ca.enter_text_in_text_box(email_textbox_elmnt, user_name)
        logger.info("gmail Username:: " + user_name)
        time.sleep(3)
        next_btn_elmnt = gmail_po.next_button_loc()
        ca.click_on_webelement(next_btn_elmnt)
        time.sleep(3)
        pwrd_tbox_loc_elmnt = gmail_po.p_word_text_box_loc()
        pwrd_tbox_loc_elmnt.send_keys(Keys.TAB)
        time.sleep(3)
        gmail_password = common_utils.AES256_decrypt(master_key, gmail_pwrd)
        pwrd_tbox_loc_elmnt.send_keys(gmail_password)
        logger.info("Given gmail passcode")
        time.sleep(3)
        next_btn_elmnt = gmail_po.next_button_loc()
        ca.click_on_webelement(next_btn_elmnt)
        time.sleep(5)
        return self.driver

    def get_ver_code_from_gmail(self, drvr, xpected_sender_name):
        gmail_po = GmailLoginPageObjectsClass(drvr)
        ca1 = CommonActionsClass(self.driver)
        element_search_gmail_button = gmail_po.search_text_loc()
        ca1.enter_text_in_text_box(element_search_gmail_button, xpected_sender_name)
        logger.info("Given " + xpected_sender_name + " in the gmail search box")
        element_search_gmail_button = gmail_po.search_gmail_button_loc()
        ca1.click_on_webelement(element_search_gmail_button)
        time.sleep(6)
        first_mes_from_name_elmnt = gmail_po.first_message_from_name_loc(xpected_sender_name)
        first_mes_from_name_elmnt.click()
        logger.info("Selected the email with verification code")
        time.sleep(3)
        message_elmnt = gmail_po.message_loc()
        mesge_elmnt_text = message_elmnt.text
        mesge_elmnt_text = re.split('\s+', mesge_elmnt_text)
        ver_code_from_gmail = mesge_elmnt_text[mesge_elmnt_text.index("Code:")+1]
        logger.info("Verification code::" + ver_code_from_gmail)
        time.sleep(3)
        signout_elmnt = gmail_po.gmail_sign_out_element()
        signout_elmnt.click()
        time.sleep(3)
        logger.info("Logged out from the Gmail")
        return ver_code_from_gmail

    def open_mail_attachment(self, drvr):
        gmail_po = GmailLoginPageObjectsClass(drvr)
        commonutil = CommonUtilsClass()
        ca1 = CommonActionsClass(self.driver)
        ca1.scroll_whole_page(self.driver)
        timestamp = commonutil.last_user_created()
        time.sleep(5)
        mail_attachment_element = gmail_po.mail_attachment_loc()
        ca1.click_on_webelement(mail_attachment_element)
        logger.info("Hovered and clicked on the mail attachment with name containing " + timestamp)
        time.sleep(2)
        return self.driver

    def open_gmail_content(self, drvr, string_to_search):
        '''
        FOt gmail standard view
        :param drvr:
        :param string_to_search:
        :return:
        '''
        gmail_po = GmailLoginPageObjectsClass(drvr)
        ca1 = CommonActionsClass(self.driver)
        time.sleep(3)
        element_search_gmail_button = gmail_po.search_text_loc()
        ca1.enter_text_in_text_box(element_search_gmail_button, string_to_search)
        logger.info("Given " + string_to_search + " in the gmail search box")
        element_search_gmail_button = gmail_po.search_gmail_button_loc()
        ca1.click_on_webelement(element_search_gmail_button)
        time.sleep(6)
        element_select_data_import_mail = gmail_po.select_data_import_mail_loc(string_to_search)
        ca1.click_on_webelement(element_select_data_import_mail)
        logger.info("Selected the first mail after the search")
        return self.driver

    def copy_attachment_content_to_textfile(self, drvr, target_filepath):
        gmail_po = GmailLoginPageObjectsClass(drvr)
        commonutil = CommonUtilsClass()
        current_window = self.driver.current_window_handle
        attachmentment_window=self.driver.window_handles[1]
        self.driver.switch_to.window(attachmentment_window)
        attachment_message_element = gmail_po.mail_attachment_message_loc()
        attachment_message_data = attachment_message_element.text
        commonutil.write_data_into_file(target_filepath, attachment_message_data)
        logger.info("Copied and pasted the error message in " + target_filepath + " file")
        self.driver.close()
        self.driver.switch_to.window(current_window)
        return self.driver

    def gmail_sign_out_html(self, drvr):
        '''
        Sign out from the gmail when gmail is in HTML view
        :param drvr:
        :return:
        '''
        gmail_po = GmailLoginPageObjectsClass(drvr)
        time.sleep(3)
        signout_elmnt = gmail_po.gmail_sign_out_element()
        signout_elmnt.click()
        time.sleep(3)
        logger.info("Logged out of the test gmail account")
