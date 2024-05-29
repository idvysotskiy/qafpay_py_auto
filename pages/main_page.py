import allure
import re
import random

from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    start_with_email_btn = '//*[@text="Start with email"]/..'
    language_selector = '//*[@text="English"]/..'
    contur_selector = '//*[@text="demo"]'
    text_edit = '//android.widget.EditText'
    continue_btn = '//*[@text="Continue"]/..'
    prod_contur = '//*[@text="qafpay.com"]'

    def get_verification_code(self, user_name):
        options = webdriver.FirefoxOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        # options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")
        options.add_argument("--lang=en-US")
        driver = webdriver.Firefox(options=options)
        driver.get(f"https://www.mailforspam.com/mail/{user_name}/1")
        code_value = int(re.sub('[^0-9]', "", driver.find_element(By.CSS_SELECTOR, "p[id='messagebody']").text))
                                            # [contains(text(), 'QafPay: Your one time password is')]").text))
        print(code_value)
        driver.close()
        return code_value

    def registration(self):
        self.click(self.contur_selector)
        self.click(self.prod_contur)
        self.click(self.start_with_email_btn)

        user_name = "test" + str(random.randint(0, 99999999))
        mail = user_name + "@mailforspam.com"

        self.set_text(self.text_edit, mail)
        self.click(self.continue_btn)

        code = str(self.get_verification_code(user_name))
        # self.click(self.text_edit)
        # self.d.send_keys(code)
        self.set_text(self.text_edit, code)
