"""Program: Module-6.py
Date of Last Edit: 3-25-2024
Author: Benjamin Thomas Raleigh
Purpose of Code: Retrieve
"""
from urllib.request import urlopen
import json

try:
    response = urlopen('https://api.openf1.org/v1/race_control')
    data = json.loads(response.read().decode('utf-8'))
except OSError as err:
    print(err)
except TypeError as err:
    print(err)
