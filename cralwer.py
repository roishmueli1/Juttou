from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import os
import json
import re
import time
# import datetime

chrome_path = r'C:\Users\Roi Shmueli\Downloads\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(chrome_path)
posts = []
browser.get('https://www.facebook.com/juttoujewelry/')

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
i = 1

while True:
	# Scroll down to bottom
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# Wait to load page
	time.sleep(SCROLL_PAUSE_TIME)
	# Calculate new scroll height and compare with last scroll height
	new_height = browser.execute_script("return document.body.scrollHeight")
	# if new_height == last_height:  break
	last_height = new_height
	i = i+1
	if(i>200):
		break

element = browser.find_elements_by_class_name('userContentWrapper')
j=1
for i in element:
    time1 = i.find_element_by_class_name('_5ptz')
    time2 = time1.get_attribute("title")

    print(time2)

    contents = i.find_elements_by_tag_name('p')
    content = '';
    if len(contents) > 0:
    	# print(len(contents))
    	for c in contents:
    		content = content + c.text

    content = content.replace("\n", " ")
    content = content.replace("...", " ")
    content = content.replace('"', "'")
    try:
        post = {}
        post["time"] = time2
        post["number"] = j
        post["content"] = content
        posts.append(post)
    except AttributeError:
    	pass
    j+=1
filename = "data1.json"
with open(filename, mode='w', encoding='utf-8') as f:
    json.dump(posts, f, indent=2,  ensure_ascii=False)

browser.quit()
