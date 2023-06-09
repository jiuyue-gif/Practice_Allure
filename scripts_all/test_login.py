from time import sleep

from base.base_driver import init_driver
from base.base_yml import yml_data_with_file
from page.login_page import LoginPage
import allure, pytest
import os, sys
sys.path.append(os.getcwd())


def data_with_key(key):
    return yml_data_with_file("login_data")[key]


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.login_page = LoginPage(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step(title="登录的测试脚本")
    # 参数化测试用例
    @pytest.mark.parametrize("username,password,toast,screen", data_with_key("login information"))
    def test_login(self, username, password, toast, screen):
        print(username + " " + password + " " + toast + " " + screen)
        # 下方的allure.attach("点击切换密码登录", "")是allure报告的解释步骤
        allure.attach(name="点击切换密码登录", body="")
        self.login_page.click_change_password()
        allure.attach(name="点击用户名输入框", body="")
        self.login_page.click_username()
        allure.attach(name="清除用户名输入框", body="")
        self.login_page.clear_username()
        # 默认前边的是body，后边的是name。name显示在上一级，所以上一级写在后边。
        allure.attach("", "输入用户名" + username)
        self.login_page.input_username(username)
        allure.attach("", "输入密码" + password)
        self.login_page.input_password(password)
        allure.attach(name="勾选同意协议", body="")
        self.login_page.click_check_agreement()
        allure.attach(name="点击登录", body="")
        self.login_page.click_login()
        sleep(2)
        allure.attach(name="截图生成的结果", body="")
        self.login_page.screenshot(screen)
        allure.attach(open("./screen/" + screen + ".png", "rb").read(), "图片", allure.attachment_type.PNG)
        # allure.attach("判断对应的提示是否存在", toast)
        # assert self.login_page.is_toast_exist(toast, True, screen)
