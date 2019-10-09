# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:32:54 2019

@author: DSC
"""

#youtube test file

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
d = webdriver.Chrome()
driver.get('https://www.google.com')
d.get('https://www.youtube.com/results?search_query=memories')
driver.close()