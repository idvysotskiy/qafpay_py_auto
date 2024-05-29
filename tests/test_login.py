import time

import allure
import pytest
import uiautomator2 as u
from selenium import webdriver
from pages.main_page import MainPage

d = u.connect("emulator-5554")


@pytest.mark.usefixtures("setup")
@allure.feature("Профиль")
class TestProfile:

    @allure.title("Регистрация")
    @pytest.mark.smoke
    def test_registration(self):
        page = MainPage()
        page.registration()


