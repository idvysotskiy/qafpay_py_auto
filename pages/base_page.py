import random
import time
from tests.config import *
import allure
import uiautomator2 as u
from faker import Faker
from uiautomator2 import Direction


class BasePage:
    d = u.connect(device_id)
    faker = Faker()

    def click(self, locator, element_name=None):
        if not isinstance(locator, str):
            if element_name is not None:
                with allure.step(f"Клик по элементу '{element_name}'"):
                    locator.click()
                    self.wait_a_moment()
                    self.get_screen()
            else:
                locator.click()
                self.wait_a_moment()
                self.get_screen()
        else:
            if element_name is not None:
                with allure.step(f"Клик по элементу '{element_name}'"):
                    self.get_element(locator).click()
                    self.wait_a_moment()
                    self.get_screen()
            else:
                self.get_element(locator).click()
                self.wait_a_moment()
                self.get_screen()

    def set_text(self, locator, text, element_name=None):
        if element_name is not None:
            with allure.step(f"Заполнение поля '{element_name}' текстом '{text}'"):
                self.get_element(locator).set_text(text)
        else:
            self.get_element(locator).set_text(text)

    def get_element(self, locator):
        if locator[0] == '/' and locator[1] == '/':
            return self.d.xpath(locator)
        else:
            return self.d(resourceId=locator)

    # @allure.step("Получение рандомного элемента")
    def get_random_element(self, locator):
        if isinstance(locator, str):
            if locator[0] == '/' and locator[1] == '/':
                counter = random.randrange(0, len(self.d.xpath(locator).all()) - 1)
                elements_list = self.d.xpath(locator).all()
                return elements_list[counter]
            else:
                counter = random.randrange(0, self.d(resourceId=locator).count - 1)
                return self.d(resourceId=locator)[counter]
        else:
            counter = random.randrange(0, locator.count - 1)
            return locator[counter]

    def get_text(self, locator):
        return self.get_element(locator).get_text()

    def wait_a_moment(self):
        time.sleep(0.5)

    def wait_a_second(self):
        time.sleep(1)

    def get_screen(self):
        screen = "screen.png"
        self.d.screenshot(screen)
        allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)

    @allure.step("Свайп вверх")
    def swipe_up(self, count=None):
        if count is not None:
            for i in range(count):
                # self.d.swipe(self.d.window_size()[0] / 2, self.d.window_size()[1] / 2, self.d.window_size()[0] / 2,
                #              self.d.window_size()[1] / 4)
                self.d.swipe_ext(Direction.FORWARD)
        else:
            # self.d.swipe(self.d.window_size()[0] / 2, self.d.window_size()[1] / 2, self.d.window_size()[0] / 2,
            #              self.d.window_size()[1] / 4)
            self.d.swipe_ext(Direction.FORWARD)

    @allure.step("Свайп вниз")
    def swipe_down(self):
        self.d.swipe(self.d.window_size()[0] / 2, self.d.window_size()[1] / 4, self.d.window_size()[0] / 2,
                     self.d.window_size()[1] / 2)

    # @allure.step("Свайп к элементу")
    def swipe_to_element(self, locator):
        for i in range(10):
            if self.get_elements_amount(locator) == 0:
                self.swipe_up()
                self.wait_a_second()
            else:
                self.wait_element(locator)
                break

    def swipe_down_to_element(self, locator):
        for i in range(10):
            if self.get_elements_amount(locator) == 0:
                self.swipe_down()
                self.wait_a_second()
            else:
                self.wait_element(locator)
                break

    def swipe_coordinate(self, fx, fy, tx, ty):
        self.d.swipe(fx, fy, tx, ty, duration=0.1, steps=None)

    # @allure.step("Ожидание элемента")
    def wait_element(self, locator, element_name=None):
        if element_name is not None:
            with allure.step(f"Ожидание элемента '{element_name}'"):
                if isinstance(locator, str):
                    if locator[0] == '/' and locator[1] == '/':
                        assert self.get_element(locator).exists == True, print(f"Элемент {element_name} отсутствует")
                    else:
                        assert self.get_element(locator).wait(10) == True, print(f"Элемент {element_name} отсутствует")
                else:
                    assert locator.wait(10) == True, print(f"Элемент {element_name} отсутствует")
        else:
            if isinstance(locator, str):
                if locator[0] == '/' and locator[1] == '/':
                    assert self.get_element(locator).exists == True
                else:
                    assert self.get_element(locator).wait(10) == True
            else:
                assert locator.wait(10) == True

    # @allure.step("Ожидание отсутствия элемента")
    def wait_hidden_element(self, locator, element_name=None):
        if element_name is not None:
            with allure.step(f"Ожидание отсутствия элемента '{element_name}'"):
                if isinstance(locator, str):
                    if locator[0] == '/' and locator[1] == '/':
                        assert self.get_element(locator).exists == False, print(
                            f"Элемент {element_name} присутствует на экране")
                    else:
                        assert self.get_element(locator).wait_gone(5) == True, print(
                            f"Элемент {element_name} присутствует на экране")
                else:
                    assert locator.wait_gone(5) == True, print(f"Элемент {element_name} присутствует на экране")
        else:
            if isinstance(locator, str):
                if locator[0] == '/' and locator[1] == '/':
                    assert self.get_element(locator).exists == False
                else:
                    assert self.get_element(locator).wait_gone(5) == True
            else:
                assert locator.wait_gone(5) == True

    def checking_exists_element(self, locator, element_name=None):
        if element_name is not None:
            with allure.step(f"Ожидание элемента '{element_name}'"):
                assert self.get_element(locator).exists == True, print(element_name + " отсутствует")
        else:
            assert self.get_element(locator).exists == True

    @allure.step('Press back')
    def press_back(self):
        self.d.press('back')

    @allure.step("Ожидание элемента с текстом '{text}'")
    def wait_text(self, text):
        assert self.d(textContains=text).wait(10) == True, print(f"Элемент с текстом {text} отсутствует")

    @allure.step("Ожидание на экране alertTitle '{title}'")
    def wait_alert_title(self, title):
        assert self.d(resourceId='com.yapmap.yapmap:id/alertTitle',
                      textContains=f'{title}').wait(10) == True, print(f"Отсутствует заголовок {title}")

    @allure.step("Ожидание на экране заголовка '{title}'")
    def wait_title_text(self, title):
        assert self.d(resourceId='com.yapmap.yapmap:id/title_text_view',
                      textContains=f'{title}').wait(10) == True, print(f"Отсутствует заголовок {title}")

    # @allure.step("Получение количества элементов")
    def get_elements_amount(self, locator):
        if locator[0] == '/' and locator[1] == '/':
            return len(self.get_element(locator).all())
        else:
            return self.get_element(locator).count

