import urllib.request
from bs4 import BeautifulSoup
def hasSeats(CRNlist, season, semesterNumber):
	available = []
	cntr = 0;
	for CRN in CRNlist:
		url = 'http://ssb.cc.binghamton.edu/banner/bwckschd.p_disp_detail_sched?term_in='+ semesterNumber + '&crn_in=' + str(CRN);
		#^^forms the url for checking if a course has open seats.
		page = urllib.request.urlopen(url);
		#requests the html of a page using urllib.request
		soup = BeautifulSoup(page, 'html.parser');
		#saves all the html in soup -- think of it like a big string of html
		testTag = soup.find_all("td", class_="dddefault");
		#searches for the tags in the html containing the seat numbers.
		#in this case the seats are in the html code class = dddefault
		str1 = int(testTag[2].string);
		#testTag is a list of size 3, containing a big html tag subsections
		#as testag[0], the capacity as testTag[1], and the available seats as
		#testTag2
		print("the course has " + str(str1) + " available seats out of " + str(testTag[1].string) + " total seats in the class")
		if(str1>0):
			available.append(True)
			cntr = cntr + 1
		else:
			available.append(False)
	if(cntr > 0):
		available.append(True)
	else:
		available.append(False)
	return available;
