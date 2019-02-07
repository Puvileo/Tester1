# -*- coding: utf-8 -*-
import unittest, time, re
from selenium import webdriver
from PIL import ImageGrab
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

listNP = [('slawakp@mail.ru', '1Qaz2wsx+'), ('slavak@mail.ru', '1Qaz2wsx+'), ('slavakp', '12345'),
          ('slavakpss@mail.ru', '1Qaz2wsx+')]


class newbook(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(10) # падла всё тормозит, не успеват при 30 всё обскакать
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_newbook(self):

        driver = self.driver #чтоб не повторяться с self
        driver.get("https://newbookmodels.com/auth/signin")
        j, k, l, m = 0, 0, 0, 0
        for i in range(4):
            email = driver.find_element_by_xpath('//input')
            email.click()
            email.clear()
            email.send_keys(listNP[i][0])
            password = driver.find_element_by_xpath(
                '//nb-form-group[2]/div/div[2]/div[2]/content/common-input/label/input')
            password.click()
            password.clear()
            password.send_keys(listNP[i][1])
            self.driver.find_element_by_xpath('//button').click()
            time.sleep(3)
            if driver.find_elements_by_xpath("//*[contains(text(), 'Please enter a correct')]"):
                print('email', listNP[i][0], 'and/or password are not correct')
                if j < 1:
                    #self.image(i)
                    image = ImageGrab.grab()
                    name_image = 'E:\TMP\image' + str(i) + '.jpg'
                    image.save(name_image, 'JPEG')
                    j += 1
            elif driver.find_elements_by_xpath("//*[contains(text(), 'email address')]"):
                print('email', listNP[i][0], 'is not correct')
                if k < 1:
                    #self.image(i)
                    image = ImageGrab.grab()
                    name_image = 'E:\TMP\image' + str(i) + '.jpg'
                    image.save(name_image, 'JPEG')
                    k += 1
            elif driver.find_element_by_xpath("//*[contains(text(), 'is blocked')]"):
                print('account with email', listNP[i][0], 'and password', listNP[i][1], 'is blocked')
                if l < 1:
                    #self.image(i)
                    image = ImageGrab.grab()
                    name_image = 'E:\TMP\image' + str(i) + '.jpg'
                    image.save(name_image, 'JPEG')
                    l += 1
            else:
                print('pass')
                #self.image(i)
                image = ImageGrab.grab()
                name_image = 'F:\TMPmy\image' + str(i) + '.jpg'
                image.save(name_image, 'JPEG')
            time.sleep(3)



    def image(self, i):
        self.image = ImageGrab.grab()
        name_image = 'E:\TMP\image' + str(i) + '.jpg'
        self.image.save(name_image, 'JPEG')

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    @property
    def is_alert_present(self):
        try:
            # self.driver.switch_to_alert()
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
