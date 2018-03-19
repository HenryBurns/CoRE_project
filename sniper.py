import time;
from selenium import webdriver;
from bs4 import BeautifulSoup;
def register(username, password, CRN):
	login_url = 'https://ssb.cc.binghamton.edu/banner/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu&msg=WELCOME+Welcome+to+BU+BRAIN+Self+Service'
	browser = webdriver.Firefox();
	#makes a firefox browser
	browser.get(login_url) 
	#opens the browser to login url
	username1 = browser.find_element_by_name("sid")
	password1 = browser.find_element_by_name("PIN")
	#select the username and password inputs in the browser
	username1.send_keys(username)
	password1.send_keys(password)
	#fill in the afformentioned inputs with username and password
	browser.find_element_by_xpath("//input[@value='Login' and @type='submit']").click()
	time.sleep(1);
	browser.find_element_by_link_text("Student").click()
	time.sleep(1);
	#switch windows in bu brain and click on student
	browser.find_element_by_link_text("Registration").click()
	#click registration
	time.sleep(1)
	browser.find_element_by_link_text("Add/Drop or Withdraw from a Course").click()
	#click add/drop
	time.sleep(1)
	seasons = browser.find_elements_by_css_selector('option.value')
	#get all the possible semester selections
	for temp in seasons:
		if lower(temp.text) == lower(season + " " + year):
			temp.click();
	#click only the semester that matches what was requested
	browser.find_element_by_xpath("//input[@value='Submit' and @type='submit']").click();
	#submit the semester
	username1 = browser.find_element_by_id("crn_id1")
	#put in crn
	username1.send_keys(CRN)
	#put the data in the website
	#browser1.find_element_by_link_text("Submit Changes").click()
