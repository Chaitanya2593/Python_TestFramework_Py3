'''

Created on March 2018
Framework Conceived by : Venkata
@author: Venkata
'''
from ActionsAll.common_actions import CommonActionsClass
from commonVariables import gmail_uname
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GmailLoginPageObjectsClass(object):
    def __init__(self, driver):
        '''
        this is a constructor of class
        :param driver:
        '''
        self.driver = driver

    def email_text_box_loc(self):
        '''
        Comments:: Gmail username field
        :return:
        '''
        ca1 = CommonActionsClass(self.driver)
        locatorstrng = "//input[@type='email' and @aria-label='Email or phone' or @aria-label='E-Mail oder Telefonnummer' or @autocomplete='username']"
        is_present = ca1.element_with_fluent_wait(locatorstrng, 40)
        if is_present:
            email_text_box_element = self.driver.find_element_by_xpath(locatorstrng)
            return email_text_box_element
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def next_button_loc(self):
        locatorstring = ".//span[contains(text(),'Next') or contains(text(),'Weiter')]"
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 90)
        if is_present:
            search_button_element = self.driver.find_element_by_xpath(locatorstring)
            return search_button_element
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def p_word_text_box_loc(self):
        locatorstring = "//input[@type='password' and contains(@name,'passwor')]"
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 120)
        if is_present:
            p_word_text_box_element = self.driver.find_element_by_xpath(locatorstring)
            return p_word_text_box_element
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def account_details_element(self):
        locatorstring = "//*[contains(@aria-label,'" + gmail_uname + "')]"
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            elemnt_acct_details = self.driver.find_element_by_xpath(locatorstring)
            return elemnt_acct_details
        else:
            logger.info("Cannot determine if Element is present in 40 seconds. Locator::" + locatorstring)

    def gmail_username_element(self):
        locatorstring = "//div[following-sibling::div[child::*[contains(text(),'Privacy')]]][2]"
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            elemnt_acct_details = self.driver.find_element_by_xpath(locatorstring)
            return elemnt_acct_details
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def gmail_sign_out_element(self):
        locatorstring = "//a[contains(text(),'Sign out')]"
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            elemnt_acct_details = self.driver.find_element_by_xpath(locatorstring)
            return elemnt_acct_details
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def gmail_inbox_loc(self):
        locatorstring = "//a[contains(text(),'Inbox')]"
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            elemnt_acct_details = self.driver.find_element_by_xpath(locatorstring)
            return elemnt_acct_details
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def first_message_from_name_loc(self, mail_string):
        locatorstring = "(//span/span[ancestor::div[@role='main'] and contains(text(),'" + mail_string + "')])[2]"
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            elemnt_acct_details = self.driver.find_element_by_xpath(locatorstring)
            return elemnt_acct_details
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def search_gmail_button_loc(self):
        '''
        Works for both standard and html view
        :return:
        '''
        ca1 = CommonActionsClass(self.driver)
        locatorstring = "//*[@aria-label='Search Gmail' or @aria-label='Search Mail' or @value='Search Mail']"
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            element_search_gmail_button = self.driver.find_element_by_xpath(locatorstring)
            return element_search_gmail_button
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def search_text_loc(self):
        '''
        supports both html and Standard view
        :return:
        '''
        ca1 = CommonActionsClass(self.driver)
        locatorstring = '//*[contains(@aria-label,"Search") or contains(@title,"Search")]'
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            element_search_gmail_text_box = self.driver.find_element_by_xpath(locatorstring)
            return element_search_gmail_text_box
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def select_data_import_mail_loc(self, date_time_stamp):
        ca1 = CommonActionsClass(self.driver)
        date_time_stamp_1 = date_time_stamp[0:len(date_time_stamp) - 4]
        date_time_stamp_2 = date_time_stamp[len(date_time_stamp) - 3:len(date_time_stamp) - 1]
       #working for the standard locatorstring = "//span[ancestor::div[@role='main'] and ancestor::div[following-sibling::span[contains(text(),'" + date_time_stamp_2 + "')]]][1]"
        locatorstring = "//b[contains(text(),'Data Extension Import Notification') and following-sibling::*[child::b[contains(text(),'" + date_time_stamp_2 + "')]]][1]"

        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            element_select_data_import_mail = self.driver.find_element_by_xpath(locatorstring)
            return element_select_data_import_mail
        else:
            logger.info("Cannot determine if Element is present in 40 seconds"+locatorstring)

    def message_loc(self):
        locatorstring = ".//*[contains(@id,'')]"
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            elemnt_acct_details = self.driver.find_element_by_xpath(locatorstring)
            return elemnt_acct_details
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def mail_attachment_loc(self):

        # for standard view locatorstring = "//a[contains(@class,'') and child::*[contains(text(),'" + timestamp + "')]]"
        locatorstring = "//a[contains(text(),'View') and following-sibling::*[contains(text(),'ownload')]]"
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            mail_attachment_element = self.driver.find_element_by_xpath(locatorstring)
            return mail_attachment_element
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def mail_attachment_message_loc_std(self, timestamp):
        '''
        for standard gmail look
        :param timestamp:
        :return:
        '''
        locatorstring = "//pre[ancestor::*[contains(@aria-label,'" + timestamp + "') and contains(@aria-label,'Displaying')]]"
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            attachment_message_element = self.driver.find_element_by_xpath(locatorstring)
            return attachment_message_element
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def mail_attachment_message_close_loc(self):
        locatorstring = '//*[contains(@aria-label,"Close") and contains(@data-tooltip,"Close")]'
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            mail_attachment_message_close_element = self.driver.find_element_by_xpath(locatorstring)
            return mail_attachment_message_close_element
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")

    def mail_attachment_message_loc(self):
        '''
        for html gmail look
        :param timestamp:
        :return:
        '''
        locatorstring = "//*[contains(@style,'word-wrap')]"
        ca1 = CommonActionsClass(self.driver)
        is_present = ca1.element_with_fluent_wait(locatorstring, 40)
        if is_present:
            attachment_message_element = self.driver.find_element_by_xpath(locatorstring)
            return attachment_message_element
        else:
            logger.info("Cannot determine if Element is present in 40 seconds")
