import main
import getpass
import datetime
def inputs():
	CRNlist = []
	CRNlist.append(input("CRN: "));
	moreClasses = input("If you want to register for additional classes type 'y': ")
	while(moreClasses == "y"):
		CRNlist.append(input("CRN: "))
		moreClasses = input("If you want to register for additional classes type 'y': ")
	#take the CRN as an arg
	#TODO add a searching method for the course provided number and 
	#type of course
	season = input("Semester season (spring, fall etc): ");
	season = season.lower();
	user = input("Username: ");
	passw = getpass.getpass('Password:')
	for CRN in CRNlist:
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
	#code used by bubrain to get get the semester and year for a course
	main.main(CRNlist, user, passw, season, semesterNumber);
	#call the actuall function, it will loop until completed
inputs()
