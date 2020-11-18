from selenium import webdriver
import time
for i in range (0,2):
 options = webdriver.ChromeOptions()
 options.add_argument("user-data-dir=C:/Users/USER/AppData/Local/Google/Chrome/User Data")

 driver = webdriver.Chrome(executable_path="F://henry/bot project/chromedriver", options=options)
 searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
 searchbox.send_keys('Master teaser')

 searchbutton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
 searchbutton.click()

 youtube = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div/div[1]/a/span')
 youtube.click()

 time.sleep(100)
 driver.close()
