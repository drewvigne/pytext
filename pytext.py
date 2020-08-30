"""
Author: Drew Vigne

Script that sends text message notifications via gmail 
SMTP server.

Credits: Some guy on reddit.

Created: 8/29/2020
"""

import smtplib

carriers = {
	'att':      '@mms.att.net',
	'tmobile':  '@tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send(message):
    # Replace with your number and carrier
	to_number = '0000000000{}'.format(carriers['**carrier**'])
    # Replace with your gmail and password, burner account recommended
	auth = ('**gmail**', '**password**')

    # Establish connection with SMTP server
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(auth[0], auth[1])

    # Send the sms
	server.sendmail(auth[0], to_number, message)

