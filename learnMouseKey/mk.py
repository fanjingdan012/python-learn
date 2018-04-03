import pyautogui
pyautogui.PAUSE = 2
pyautogui.moveTo(300, 300);
#pyautogui.click(300, 300)
while 1:
#for i in range(200):
    # print(i)
    #pyautogui.scroll(-100)

    pyautogui.moveTo(300, 300, duration=0.75)
    pyautogui.moveTo(300, 400, duration=0.75)
#
#
# pyautogui.click(500, 200)
# pyautogui.typewrite('Hello world!',0.25)

# for i in range(10):
#       pyautogui.moveTo(300, 300, duration=0.25)
#       pyautogui.moveTo(400, 300, duration=0.25)
#       pyautogui.moveTo(400, 400, duration=0.25)
#       pyautogui.moveTo(300, 400, duration=0.25)

# from PIL import ImageGrab
#
# im = ImageGrab.grab()
#
# im.save("E:\\a.jpg",'jpeg')

# coding=utf-8
import time
from selenium import webdriver

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()