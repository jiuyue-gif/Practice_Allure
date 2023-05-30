from appium import webdriver


def init_driver():
    # server启动参数
    desired_caps = dict()
    # 设备信息
    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = "8.0"
    desired_caps["deviceName"] = "192.168.56.1:4723"
    # app信息
    desired_caps["appPackage"] = "com.yunmai.scale"
    desired_caps["appActivity"] = ".ui.activity.login.mvvm.LoginMvvmActivity"
    # 中文
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True
    # 声明对象
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver


if __name__ == "__main__":
    ele = init_driver()
