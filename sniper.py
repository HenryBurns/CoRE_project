import time;
from selenium import webdriver;
from bs4 import BeautifulSoup;
def register(username, password, CRN):
	login_url = 'https://cas.cc.binghamton.edu/cas/login?service=https%3A%2F%2Fmy.binghamton.edu';
	#the url to log in to mybinghamton
	#new_url = 'https://ssb.cc.binghamton.edu/banner/bwskfreg.P_AltPin';
	#the ur
	browser = webdriver.Firefox();
	#makes a firefox browser
	browser.get(login_url) 
	#opens the browser to login url
	username1 = browser.find_element_by_id("username")
	password1 = browser.find_element_by_id("password")
	#select the username and password inputs in the browser
	username1.send_keys(username)
	password1.send_keys(password)
	#fill in the afformentioned inputs with username and password
	browser.find_element_by_name("submit").click()
	time.sleep(1);
	#TODO optimize this we can go directly to this website and log
	#in to avoid ~7 seconds of wait
	#browser.get('https://ssb.cc.binghamton.edu/banner/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu&msg=WELCOME+Welcome+to+BU+BRAIN+Self+Service');
	#just got through login screen
	browser.find_element_by_xpath("/html/body/section/header/div[2]/ul[1]/li/div/a[1]").click()
	#if this doesn't work go to bu brain and click inspect element on my 
	#dashboard in google chrome on top of the bu brain icon. from there
	#right click the highlighted line, click copy Xcode, and put it in here.
	time.sleep(1)
	#select bu brain
	main_window = browser.window_handles[1];
	browser.switch_to_window(main_window)
	time.sleep(1)
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
			break;
	#click only the semester that matches what was requested
	browser.find_element_by_xpath('/html/body/div[3]/form/input').click()
	#submit the semester
	username1 = browser.find_element_by_id("crn_id1")
	#put in crn
	username1.send_keys(CRN)
	#put the data in the website
	#browser1.find_element_by_link_text("Submit Changes").click()
