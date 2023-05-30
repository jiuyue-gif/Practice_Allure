from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import os, sys
sys.path.append(os.getcwd())


class LoginPage(BaseAction):
    # 切换密码登录按钮、账号输入框、密码输入框、勾选协议按钮、登录按钮
    # 如果使用xpath的定位方法:单条件拼接格式：“text,设置,0”，0代表包含查找(不填写代表默认0)，1代表精准查找；多条件拼接格式：["text,设置,1", "text,设置"]
    agree_continue_button = By.ID, "com.yunmai.scale:id/auth_btn_agree"
    change_password_button = By.ID, "com.yunmai.scale:id/tv_selection_password"
    username_box = By.ID, "com.yunmai.scale:id/edt_phone"
    # username_box = By.XPATH, "resource-id,com.yunmai.scale:id/edt_phone"
    password_box = By.ID, "com.yunmai.scale:id/edt_password"
    check_agreement_button = By.ID, "com.yunmai.scale:id/login_service_checkbox"
    login_button = By.ID, "com.yunmai.scale:id/btn_login"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # 点击同意并继续
        self.click(self.agree_continue_button)

    # 点击切换密码登录
    def click_change_password(self):
        self.click(self.change_password_button)

    # 点击同意协议
    def click_check_agreement(self):
        self.click(self.check_agreement_button)

    # 点击登录
    def click_login(self):
        self.click(self.login_button)

    # 点击用户名输入框
    def click_username(self):
        self.click(self.username_box)

    # 清除用户名输入框
    def clear_username(self):
        self.clear(self.username_box)

    # 输入用户名
    def input_username(self, text):
        self.input(self.username_box, text)

    # 输入密码
    def input_password(self, text):
        self.input(self.password_box, text)

    # 判断对应的提示是否存在
    # def is_toast_exist(self, toast):
    #     pass
