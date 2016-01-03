###############################################################
#
#				Jiwan Ninglekhu
#				01/01/2016
#				AutoStatus
#				Language: Python
#
################################################################

from bs4 import BeautifulSoup
import requests
import re
import time
import unittest
from urllib2 import HTTPError
import urllib as UR
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import *


try:
	linky = "http://computerworld.com"
	page = UR.urlopen(linky)
except IOError:
	print("URL Not Found")
		#continue
else:

	soup = BeautifulSoup(page.read(), "html.parser")
	htag = soup.find({"h3"}) 
	# for h in htag:
	# 	print h	

	for link in soup.findAll("a"):
		if 'href' in link.attrs: 
			thelink = link.attrs['href']
			thelink = linky + thelink
			print thelink
			break
		

	firstone = soup.findAll("a")
	firsttext = (firstone[0].get_text())
	print firsttext
print "Source website scraped and first intended link taken"


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.linkedin.com/")

print "Destination website fired-up!"

linkedinUsername = "jiwan.ninglekhu@hotmail.com"
linkedinPassword = "Limbu123"
emailFieldID   = "login-email"
passFieldID    = "login-password"
loginButtonName = "submit"
inLogoID 	   = "in-logo"

emailFieldElement = driver.find_element_by_id(emailFieldID)
passFieldElement = driver.find_element_by_id(passFieldID)
loginButtonElement = driver.find_element_by_name(loginButtonName)

emailFieldElement.clear()
emailFieldElement.send_keys(linkedinUsername)
passFieldElement.clear()
passFieldElement.send_keys(linkedinPassword)
loginButtonElement.click()
#implicit driver for 5 seconds wait before the click action is done
driver.implicitly_wait(5) # This line doesn't seem to be working ---need revision
#WebDriverWait(driver, 10).until(lambda driver: find_element_by_value(inLogoID )) #try this line

shareButtonElement = driver.find_element_by_xpath("//button[contains(., 'Share an update')]")
shareButtonElement.click()
sharePostElement = driver.find_element_by_id("postmodule-text")
driver.implicitly_wait(5)
sharePostElement.send_keys(firsttext+"\n"+thelink)
#implementing 'sleep' instead of implicit wait
time.sleep(5)
#driver.implicitly_wait(10)
shareButton1Element = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[5]/div/div[2]/div/form[1]/div[4]/div[2]/button") #"//button[contains(., 'Share')]")
shareButton1Element.click()
print "Submit button clicked"
driver.implicitly_wait(30)
driver.close()

