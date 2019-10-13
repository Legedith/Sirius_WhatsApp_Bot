# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:58:56 2018

@author: Legedith
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
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
        if target == True:
            lold = len(cmnd)
            clean = decoded(cmnd[-1])
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
            name = cmd[1]
            focus(name)
            msg_box.send_keys("Things just got a hell lot more interesting... "+Keys.RETURN)
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
            name = cmd[1]
            focus(name)
            if(cmd[2] == 'in'):
                mode = 'message-in'
            else:
                mode = 'message-out'
            msg_box.send_keys("Things just got a hell lot more interesting... "+Keys.RETURN)
            
        else:
            msg_box.send_keys("Couldn't Disapparate, Focus harder"+Keys.RETURN)
            
    elif cmd[0] == 'google' or cmd[0] == 'alohomora':
        if(len(cmd)>1):
            subject = ' '.join(cmd[1:])
            msg_box.send_keys('https://www.google.com/search?q='+removeSpaces(subject)+Keys.RETURN)
        else:
            msg_box.send_keys("No doors to open!"+Keys.RETURN)

    elif cmd[0] == 'urban':
        if(len(cmd)>1):
            subject = ' '.join(cmd[1:])
            search = urban_dict(removeSpaces(subject))
            msg_box.send_keys(search+Keys.RETURN)
        else:
            msg_box.send_keys("Hear, Hear!"+Keys.RETURN)

    elif cmd[0] == 'wiki':
        if(len(cmd)>1):
            subject = ''.join(cmd[1:])
            search = wiki(removeSpacesWiki(subject))
            msg_box.send_keys(search+Keys.RETURN)
        else:
            msg_box.send_keys("Hear, Hear!"+Keys.RETURN)
    
    elif cmd[0] == 'youtube' or cmd[0] == 'accio':
        if(len(cmd)>1):
            subject = ' '.join(cmd[1:])
            link = youtube(subject)
            msg_box.send_keys(link)
#            time.sleep(2)
            msg_box.send_keys(Keys.ENTER)
        else:
            msg_box.send_keys("Concentrate harder on the object!"+Keys.RETURN)
    
    elif cmd[0] == 'soundcloud' or cmd[0] == 'cantis':
        if(len(cmd)>1):
            subject = ' '.join(cmd[1:])
            link = soundcloud(subject)
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

def soundcloud(subject):
    d = webdriver.Chrome()    
    d.get('https://www.soundcloud.com/search?q='+removeSpaces(subject))
    vid =  d.find_elements_by_class_name('soundTitle__title')[1]
    link = vid.get_attribute('href')
    d.close()
    return link

def urban_dict(query):
    d = webdriver.Chrome()
    d.get('https://www.urbandictionary.com/define.php?term='+removeSpaces(query))
    meaning = d.find_element_by_class_name('meaning').text
    d.close()
    return meaning

def wiki(query):
    d = webdriver.Chrome()
    d.get('https://en.wikipedia.org/wiki/'+removeSpacesWiki(query))
    meaning = d.find_elements_by_tag_name('p')

    definition = ""
    for text in meaning[:4]:
        definition += text.text
    d.close()
    return definition


def spam(cmd):
    text = ' '.join(cmd[:-1])
    for i in range(int(cmd[-1])):
                msg_box.send_keys(text+Keys.RETURN)
def decoded(c):
    return c.text.split()

def removeSpaces(s):
    return s.replace(" ",'+')

def removeSpacesWiki(s):
    """
    Wikipedia uses underscores instead of '+' on their links
    """
    return s.replace(" ",'_')    

def focus(name):
    global search
    global msg_box
    search = driver.find_element_by_class_name('_2zCfw')
    search.click()
    search.send_keys(name)
    search.send_keys(Keys.RETURN)
    msg_box = driver.find_element_by_class_name('_3u328')

if __name__ == "__main__":
    while True:
        try:
            main()
        except:
            print('got an error here!')
        
        