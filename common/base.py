"""
1.学习目标
    掌握base类封装,对selenium做的二次封装
2.操作步骤
    2.1 封装打开浏览器(方法)
        def open_browser()
    2.2 建立Base类
        class Base:
            1.输入网址
            2.元素定位
            3.元素操作
3.总结
    base.py文件是可以复用,适用于任何项目中
"""
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def open_browser(browser):
    """打开浏览器"""
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "ie":
        driver = webdriver.Ie()
    else:
        print("你选择的浏览器不存在")
    return driver


class Base:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """打开网址"""
        self.driver.get(url)
        self.driver.maximize_window()  # 窗口最大化

    def find_element(self, locator, timeout=10):
        """定位单个元素"""
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        """定位一组元素"""
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator, timeout=10):
        """点击元素"""
        element = self.find_element(locator, timeout)
        element.click()

    def send_keys(self, locator, text, timeout=10):
        """元素输入"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self, locator, text, timeout=10):
        """判断文本是否在元素中"""
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value, timeout=10):
        """判断元素的value属性值是否与value相等"""
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def close_browser(self):
        """关闭浏览器"""
        self.driver.quit()


if __name__ == '__main__':
    driver = open_browser("chrome")
    base = Base(driver)
    url = "http://www.baidu.com/"
    base.open_url(url)
    time.sleep(3)
    locator_input = ("id", "kw")
    base.send_keys(locator=locator_input, text="索隆")
    time.sleep(1)
    locator_click = ("id", "su")
    base.click(locator=locator_click)
    time.sleep(5)
    locator_tp = ("link text", "图片")
    text = "图片"
    result = base.is_text_in_element(locator=locator_tp, text=text)
    print(result)
    base.close_browser()
