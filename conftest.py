import pytest
import uiautomator2 as u
from tests.config import *
from pages.base_page import BasePage

d = u.connect(device_id)


def open_app():
    d.implicitly_wait(10)
    # d.app_install("/home/qasquad/Загрузки/yapmap.apk")
    d.press('home')
    d.app_clear("team.self.qafpay")
    d.app_start("team.self.qafpay")


def teardown():
    BasePage().get_screen()
    d.app_clear("team.self.qafpay")
    d.app_stop("team.self.qafpay")


@pytest.fixture()
def setup(request):
    open_app()
    yield
    teardown()

