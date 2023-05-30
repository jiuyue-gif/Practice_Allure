from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, time=10, poll=1):
        by = loc[0]
        value = loc[1]
        # 判断，如果使用xpth的方式定位，就调用xpath拼接方法
        # if by == "By.Xpath":
        #     value = self.make_xpath_with_feature(value)
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, loc, time=10, poll=1):
        by = loc[0]
        value = loc[1]
        # 判断，如果使用xpth的方式定位，就调用xpath拼接方法
        # if by == "By.Xpath":
        #     value = self.make_xpath_with_feature(value)
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_elements(by, value))

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, text):
        self.driver.find_element(loc[0], loc[1]).send_keys(text)

    def clear(self, loc):
        self.driver.find_element(loc[0], loc[1]).clear()

    def make_xpath_with_unit_feature(self, loc):
        args = loc.split(",")
        feature = ""
        if len(args) == 2:
            feature = "contains(@" + args[0] + ",'" + args[1] + "')" + "and "
        elif len(args) == 3:
            if args[2] == "1":
                feature = "@" + args[0] + "='" + args[1] + "'" + "and "
            elif args[2] == "0":
                feature = "contains(@" + args[0] + ",'" + args[1] + "')" + "and "

        return feature

    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            if loc.startswith("//"):
                return loc
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)

        feature = feature.rstrip("and ")
        loc = feature_start + feature + feature_end
        return loc

