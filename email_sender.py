import sendgrid
import os
from sendgrid.helpers.mail import *
def send(username, CRN, season, error ):
	sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
	from_email = Email("CourseRegistration@Henry.Binghamton.edu")
	to_email = Email(username + "@binghamton.edu")
	subject = "Course Registration Status: "
	if (error):
		subject += "Success"
	else:
		subject += "Failure"
	message = "you have successfully registered for the class with the CRN "
	message += str(CRN) + " for the " + season + " semester."
	content = Content("text/plain", message)
	mail = Mail(from_email, subject, to_email, content)
	print(from_email)
	print(to_email)
	print(subject)
	response = sg.client.mail.send.post(request_body=mail.get())
	print(response.body)
