# -*- coding: utf-8 -*-
"""
Created on Wed May 19 11:31:26 2021

@author: c-est
"""

import time
from selenium import webdriver
from modules import nAccounts
from modules import completeForm
from modules import generateToken
import random

users=nAccounts.nAccounts()  
auxCount=1
url="https://es.chaturbate.com/accounts/register/"
file=open("Accounts.txt","w")
proxys=['192.227.149.53:8800','198.46.133.97:8800','192.227.149.205:8800','173.208.46.133:8800','23.95.87.15:8800','198.46.133.87:8800','192.227.149.25:8800','192.227.149.199:8800','23.95.87.88:8800','173.208.46.6:8800']

for i in range(users):  
    z=random.randint(0, 9)
    PROXY = proxys[z]
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",
    }
    driver=webdriver.Chrome("absolutePath/chromedriver")
    driver.get(url)
    userName,password,email,birthday,genderUser=completeForm.completeForm(driver)                                                               
    formToken=generateToken.generateToken(url)
    driver.execute_script("document.getElementById('g-recaptcha-response').style.display = 'flex';")
    captchaResponse=driver.find_element_by_name('g-recaptcha-response').send_keys(formToken)
    time.sleep(2)
    driver.find_element_by_id('formsubmit').click()
    print("----User n°:",auxCount,"----")
    print("userName:",userName)
    print("password:",password)
    print("email:",email)
    print("birthday:",birthday)
    file.write("User nº:")
    file.write("%s"%auxCount+"\n")    
    file.write("userName:")
    file.write("%s"%userName+"\n")
    file.write("password:")
    file.write("%s"%password+"\n")
    file.write("email:")
    file.write("%s"%email+"\n")
    file.write("birthday:")
    file.write("%s"%birthday+"\n")
    file.write("----\n")
    auxCount=auxCount+1
    time.sleep(5)
    driver.close()

print("finished")
file.close()
