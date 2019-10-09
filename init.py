# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:58:56 2018

@author: Legedith
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = 'Sirius'
phase = 'Sirius'
input('Scan QR code and press y once the screen has stopped loading: ')
time.sleep(5)

search = driver.find_element_by_class_name('_2zCfw')
search.click()
search.send_keys(name)
search.send_keys(Keys.RETURN)

target = False

msg_box = driver.find_element_by_class_name('_3u328')
mode = "message-out"
def main():
    global target
    cmnd = driver.find_elements_by_class_name(mode)
    lold = len(cmnd)
    while True:
        cmnd = driver.find_elements_by_class_name(mode)
        if target == True and lnew != lold:
            print(cmnd)
            lold = len(cmnd)
            print(lold)
            clean = decoded(cmnd[-1])
            print(clean)
            if clean[0].lower() != phase.lower():
                    continue
            execute(clean[1:-2])
            target = False
            lnew=lold
            continue
            
        lnew = len(cmnd)
        if lold < lnew:
            print(lnew-lold)
            excmd = cmnd[-(lnew-lold):]
            for c in excmd:
                clean = decoded(c)
                if clean[0].lower() != phase.lower():
                    continue
                execute(clean[1:-2])
            lold=lnew

def execute(cmd):
    global name
    global phase
    global mode
    global target
    if cmd[0] == 'spam' or cmd[0] == 'crucio':
        if(len(cmd) > 2):
            spam(cmd[1:])
        else:
            msg_box.send_keys('Crucio failed'+Keys.RETURN)
            
    elif cmd[0] == 'spam.big' or cmd[0] == 'sectumsempra':
        if(len(cmd)>3):
            focus(cmd[1])
            spam(cmd[2:])
            focus(name)
        else:
            msg_box.send_keys('Sectum Sempra failed'+Keys.RETURN)
            
    elif cmd[0] == 'change' or cmd[0] == 'apparate':
        target = True
        if(len(cmd)>1):
            focus(cmd[1])
        else:
            msg_box.send_keys("Couldn't Apparate, Focus harder"+Keys.RETURN)
            
    elif cmd[0] == 'rename' or cmd[0] == 'disapparate':
        if(len(cmd)>1):
            phase = cmd[1]
        else:
            msg_box.send_keys("Couldn't Disapparate, Focus harder"+Keys.RETURN)
    
    elif cmd[0] == 'mode' or cmd[0] == 'snape':
        target = True
        if(len(cmd)>2):
            focus(cmd[1])
            if(cmd[2] == 'in'):
                mode = 'message-in'
            else:
                mode = 'message-out'
        else:
            msg_box.send_keys("Couldn't Disapparate, Focus harder"+Keys.RETURN)
            
    elif cmd[0] == 'google' or cmd[0] == 'alohomora':
        if(len(cmd)>1):
            subject = ' '.join(cmd[1:])
            msg_box.send_keys('https://www.google.com/search?q='+removeSpaces(subject)+Keys.RETURN)
        else:
            msg_box.send_keys("No doors to open!"+Keys.RETURN)
    
    elif cmd[0] == 'youtube' or cmd[0] == 'accio':
        if(len(cmd)>1):
            subject = ' '.join(cmd[1:])
            link = youtube(subject)
            msg_box.send_keys(link)
#            time.sleep(2)
            msg_box.send_keys(Keys.ENTER)
        else:
            msg_box.send_keys("Concentrate harder on the object!"+Keys.RETURN)
    
    else:
        msg_box.send_keys('Wrong Incantation'+Keys.RETURN)
  
    
def youtube(subject):
    d = webdriver.Chrome()    
    d.get('https://www.youtube.com/results?search_query='+removeSpaces(subject))
    vid = d.find_element_by_id('video-title')
    link = vid.get_attribute('href')
    d.close()
    return link

def spam(cmd):
    text = ' '.join(cmd[:-1])
    for i in range(int(cmd[-1])):
                msg_box.send_keys(text+Keys.RETURN)
def decoded(c):
    return c.text.split()

def removeSpaces(s):
    return s.replace(" ",'+')       

def focus(name):
    global search
    global msg_box
    search = driver.find_element_by_class_name('_2zCfw')
    search.click()
    search.send_keys(name)
    search.send_keys(Keys.RETURN)
    msg_box = driver.find_element_by_class_name('_3u328')

if __name__ == "__main__":
    main()
        
        