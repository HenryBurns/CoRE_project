import urllib.request;
import sys;
import datetime;
import time;
import requests;
from selenium import webdriver;
from bs4 import BeautifulSoup;
def main(CRN, username, password, season):
	if(availible(CRN,season)):
		register(username, password);
	else:
		time.sleep(rand.randomint(30,60));
		main(CRN, username, password);
#TODO split this code into multiple modules
def availible(CRN, season):
	url = 'http://ssb.cc.binghamton.edu/banner/bwckschd.p_disp_detail_sched?term_in='+ semesterNumber + '&crn_in=' + str(CRN);
	#^^forms the url for checking if a course has open seats.
	page = urllib.request.urlopen(url);
	#requests the html of a page using urllib.request
	soup = BeautifulSoup(page, 'html.parser');
	#saves all the html in soup -- think of it like a big string of html
	testTag = soup.find_all("td", class_="dddefault");
	#searches for the tags in the html containing the seat numbers.
	#in this case the seats are contained with the html code class = dddefault
	str1 = int(testTag[2].string);
	#testTag is a list of size 3, containing a big html tag and its subsections
	#as testag[0], the capacity as testTag[1], and the available seats as
	#testTag2
	print("the course has " + str(str1) + " available seats out of " + str(testTag[1].string) + " total seats in the class")
	if(str1>0):
		return True;
	return False;
def register(username, password):
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
	time.sleep(2)
	#select bu brain
	main_window = browser.window_handles[1];
	browser.switch_to_window(main_window)
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
CRN = sys.argv[1];
#take the CRN as an arg
#TODO add a searching method for the course provided number and type of course
season = sys.argv[2];
season = season.lower();
user = sys.argv[3];
#TODO add password censoring code for taking in argument here
passw = sys.argv[4];
print("CRN: " + str(CRN) + " " + " in " + season + " session.")
szn = '';
if season == 'spring':
	szn = 20;
elif season == 'summer':
	szn = 60;
elif season == 'fall':
	szn = 90;
elif season == 'winter':
	szn = 10;
else:
	print('season (the second argument) should be spring, summer, winter, or fall');
#convert the registration session to a number used in the url for course
#registration
year = str(datetime.datetime.now().year)
#get the current registration year
semesterNumber = year + str(szn); 
#TODO rename banana with a viable variable name
main(CRN, user, passw, season);
#call the actuall function, it will loop until completed
