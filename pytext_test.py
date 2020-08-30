"""
Author: Drew Vigne

Tests the sms.py automatic text notification script.

Created: 8/29/2020
"""

import pytext

my_message = "Hello World."

pytext.send(my_message)