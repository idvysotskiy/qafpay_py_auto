import allure
import re
import random

from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.permission import Permission


class MainPage(BasePage):
    permission = Permission()

    back_btn = '//android.widget.Button/..'
    text_edit_btn_x = '//android.widget.EditText'
    start_with_email_btn = '//*[@text="Start with email"]/..'
    language_selector = '//*[@text="English"]/..'
    contur_selector = '//*[@text="demo"]'
    text_edit = '//android.widget.EditText'
    continue_btn = '//*[@text="Continue"]/..'
    prod_contur = '//*[@text="qafpay.com"]'
    later_btn = '//*[@text="Later"]/..'
    next_btn = '//*[@text="Next"]/..'
    done_btn = '//*[@text="Done"]/..'
    country_russia = '//*[@text="Russia"]/..'
    city_moscow = '//*[@text="Moscow"]'
    seek_bar = '//android.widget.SeekBar'
    confirm_btn = '//*[@text="Confirm"]'
    map_minus_btn = '//androidx.compose.ui.platform.ComposeView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]'
    map_plus_btn = '//androidx.compose.ui.platform.ComposeView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]'

    def get_verification_code(self, user_name):
        options = webdriver.FirefoxOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")
        options.add_argument("--lang=en-US")
        # options.page_load_strategy = 'none'
        options.page_load_strategy = 'eager'
        # options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        driver.get(f"https://www.mailforspam.com/mail/{user_name}/1")
        code_value = int(re.sub('[^0-9]', "", driver.find_element(By.CSS_SELECTOR, "p[id='messagebody']").text))
        print(code_value)
        driver.close()
        return code_value

    def registration(self):
        self.click(self.contur_selector)
        self.click(self.prod_contur)
        self.click(self.start_with_email_btn, 'кнопка Start with email')

        user_name = "test" + str(random.randint(0, 99999999))
        mail = user_name + "@mailforspam.com"

        self.set_text(self.text_edit, mail)
        self.click(self.continue_btn, 'кнопка Continue')

        code = str(self.get_verification_code(user_name))
        self.set_text(self.text_edit, code)
        self.wait_text('Enhance Your Security')
        self.click(self.later_btn, 'кнопка Leter')
        self.wait_text('WELCOME TO')
        self.click(self.continue_btn, 'кнопка Continue')

        self.click(self.next_btn, 'кнопка Next')
        self.click(self.next_btn, 'кнопка Next')
        self.click(self.next_btn, 'кнопка Next')
        self.click(self.done_btn, 'кнопка Done')

        self.wait_text('Where are you from?')
        self.click(self.country_russia, 'Russia')
        self.click(self.continue_btn, 'кнопка Continue')
        self.click(self.city_moscow, 'Moscow')
        self.click(self.continue_btn, 'кнопка Continue')
        self.permission.click_while_using_the_app()
        self.wait_text('Select the area around you')

        x, y = self.get_element(self.seek_bar).center()
        self.d.click(x, y)
        self.wait_text('2500 meters')
        self.click(self.confirm_btn, 'кнопка Confirm')
        self.wait_text('My account')





