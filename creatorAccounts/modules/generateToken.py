# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:05:36 2021

@author: c-est
"""
import requests
import time

def generateToken (url):
    sitekey='6Lf93goUAAAAAJKhC4y-Ok88s72iUJ8UX4bLQMmw'
    apiKey="yourapiKey"
    apiSubmitUrl="http://2captcha.com/in.php"
    apiRetrieveUrl='http://2captcha.com/res.php'
    curl = f"{apiSubmitUrl}?key={apiKey}&method=userrecaptcha&googlekey={sitekey}&pageurl={url}&json=1&invisible=1"
    response = requests.get(curl)
    responseId = response.json().get("request")
    curl2 = f"{apiRetrieveUrl}?key={apiKey}&action=get&id={int(responseId)}&json=1"
    time.sleep(5)
    while True:
        response2 = requests.get(curl2)
        print(response2.json())
        if response2.json().get("status") == 1:
            formToken = response2.json().get("request")
            break
        time.sleep(5)
    return formToken
