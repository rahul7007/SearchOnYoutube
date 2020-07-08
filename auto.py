# from selenium import webdriver
# import time

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.youtube.com')

# driver.find_element_by_name("search query").send_keys('python 3')
# driver.find_element_by_id("search-icon-legacy").click()

# time.sleep(5)
# driver.find_element_by_id("video-title").click()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# Navigate to url with video being appended to search_query
driver.get("https://www.youtube.com/results?search_query=" + str('video'))

# play the video
wait.until(visible((By.ID, "video-title")))
driver.find_element_by_id("video-title").click()