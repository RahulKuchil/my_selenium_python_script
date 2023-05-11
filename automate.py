from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.youtube.com/watch?v=2DD-ynCIZ4w')

time.sleep(10)
play_button = browser.find_element_by_css_selector('.ytp-play-button')
play_button.click()
time.sleep(5)
play_button.click()
time.sleep(2)
play_button.click()

player = browser.find_element_by_css_selector('#movie_player')
actions = ActionChains(browser)
actions.context_click(player).perform()

elements = browser.find_element_by_css_selector('div.ytp-menuitem:nth-child(7) > div:nth-child(2)').click()
time.sleep(10)

connectivity_speed = browser.find_element_by_css_selector('.html5-video-info-panel-content > div:nth-child(9) > span:nth-child(2) > span:nth-child(2)').text
print(f"Connectivity speed: {connectivity_speed}")
element = browser.find_element_by_css_selector('.ytp-sfn-close')
element.click()
time.sleep(10)

browser.quit()

