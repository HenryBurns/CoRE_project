import time
import BuBrain
import sniper
import email_sender
def main(CRNlist, username, password, season, semesterNumber):
	seats = BuBrain.hasSeats(CRNlist,season, semesterNumber)
	if(seats.pop):
		courses = []
		cntr = 0;
		for i in range(len(seats)-1):
			if(seats[i]):
				indx = i-cntr
				course = CRNlist[indx]
				courses.append(course)
				cntr = cntr + 1
		for course in courses:
			CRNlist.remove(course)
		error = sniper.register(username, password, courses)
		#email_sender.send(username, CRNlist, season, error)
		if(len(CRNlist) > 0):
			main(CRNlist, username, password, season, semesterNumber)
	else:
		time.sleep(rand.randomint(30,60))
		main(CRNlist, username, password, semesterNumber)
