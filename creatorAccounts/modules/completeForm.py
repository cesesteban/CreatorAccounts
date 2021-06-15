# -*- coding: utf-8 -*-
"""
Created on Sun May 23 14:58:21 2021

@author: c-est
"""
import requests
import string
import random
import time

def completeForm (driver):    
    emailAux="@gmail.com"
    months=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre" ]
    gender=["A Woman", "A Man", "A Couple", "Trans"]
    dataName=requests.get('http://namey.muffinlabs.com/name.json?count=1&type=name&frequency=all')
    dataSurame=requests.get('http://namey.muffinlabs.com/name.json?count=1&type=surname&frequency=all')
    userDataName=dataName.json()
    userDataSurname=dataSurame.json()
    generateStr=string.ascii_letters+string.digits+str('25')
    strAux="".join(random.choice(generateStr) for j in range(random.randint(3,4)))
    strAuxPassword="".join(random.choice(generateStr) for j in range(random.randint(7,10)))
    intAuxYear=random.randint(1960, 2000)
    intAuxMonth=random.randint(0, 11)
    intAuxDay=random.randint(1, 28) 
    intAuxGender=random.randint(0, 3)
    
    userName=userDataName[0]+userDataSurname[0]+strAux
    password='D1a'+strAuxPassword
    email=userName+emailAux 
    day=intAuxDay
    month=months[intAuxMonth]
    year=intAuxYear
    genderUser=gender[intAuxGender]
    birthday=str(day)+'/'+str(intAuxMonth+1)+'/'+str(year)
    
    driver.find_element_by_name('username').send_keys(userName)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('birthday_day').send_keys(day)
    driver.find_element_by_name('birthday_month').send_keys(month)
    driver.find_element_by_name('birthday_year').send_keys(year)
    driver.find_element_by_name('gender').send_keys(genderUser)    
    driver.find_element_by_name('terms').click()
    time.sleep(1)
    driver.find_element_by_name('privacy_policy').click()
    
    return userName,password,email,birthday,genderUser


