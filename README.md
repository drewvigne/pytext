# PyText
Python script that sends text message notifications using Google's free SMTP server.  

### About
PyText acts as a library that you can import into any script so long as they're in the same directory. Using the send(message) function, the user can send any text message to practically any phone number or dictionary of phone numbers. This script was made for use with automation software... basically so that every morning I get a text message telling me what I need to do for the day. While it is particularly good at this, it can be used for any SMTP-based text messaging application. 

### Requirements
- [Python 3.8.5](https://www.python.org/downloads/)
- [Spyder IDE (preffered)](https://www.spyder-ide.org/)  

## Installation
Installation is pretty simple. If installing Python for the first time be sure to add to PATH. If installing Spyder for the first time use default settings. Place pytext.py and pytext_test.py in the same directory.  

You will need to set up a gmail account for use with the SMTP protocol. I suggest you use a burner account for security reasons (e.g. instead of using yourname@gmail.com, create a new account called sms.yourname@gmail.com).  

To enable SMTP, go into Google security settings and allow "Less secure app access". It should work at this point but this sometimes requires troubleshooting.  

## Running the script
Open pytext.py in Spyder and fill out information like phone number, gmail, password, and carrier. Then open pytext_test.py and run. You should receive a text message.
