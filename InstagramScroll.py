from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from getpass import getpass

# Get account information from command line input
atname="rugdude"
myname='willyrootbeer'
pw='Password()'

# Open Chrome, go to instagram page
driver=webdriver.Chrome()
driver.get('https://instagram.com/'+atname)

# Click Sign In Button
button=driver.find_element_by_tag_name('button')
button.click()

# Sign in with username and password entered in command line
username=driver.find_element_by_name('username')
username.send_keys(myname)
password=driver.find_element_by_name('password')
password.send_keys(pw)
ActionChains(driver).send_keys(Keys.RETURN).perform()

# Give time to load, 3 seconds
time.sleep(3)

# Reload page to bypass "remember me" prompt
driver.get('https://instagram.com/'+atname)

# find number of posts and turn into integer
element=driver.find_element_by_class_name('g47SY')
posts=int(element.text.replace(',',''))

# find how many times while loop will run by dividing number of posts by 5
runs=(posts/5)

# while loop to scroll the page down until entire page is loaded and you can see the 
# first post
while runs>=0:
	runs-=1
	ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
	time.sleep(.5)



