from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import subprocess
import urllib.request
import time
import random
import os
import json
import pyautogui
import pyperclip
from pathlib import Path


googleID = "kkubunge84"
googlePW = "Kkubunge_79"

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fphotos.google.com%2Flogin%3F_gl%3D1*1y2tn12*_up*MQ..*_ga*MTkzODA1MzA1Mi4xNzE0MzUzNjk5*_ga_BVFP3BCBTR*MTcxNDM1MzY5OS4xLjAuMTcxNDM1MzY5OS4wLjAuMA..&followup=https%3A%2F%2Fphotos.google.com%2Flogin%3F_gl%3D1*1y2tn12*_up*MQ..*_ga*MTkzODA1MzA1Mi4xNzE0MzUzNjk5*_ga_BVFP3BCBTR*MTcxNDM1MzY5OS4xLjAuMTcxNDM1MzY5OS4wLjAuMA..&ifkv=AaSxoQzzvM_b17gpXhjvHZ88rK-5yc-N0WWqumpPAwWDPVGto_AdnZlJVJ-JX4rES_i9S3Vgd-zClw&osid=1&passive=1209600&service=lh2&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1611420408%3A1714353706904098&theme=mn&ddm=0')
# driver.implicitly_wait(5)

# e = driver.find_element(By.CSS_SELECTOR, "#identifierId")
# time.sleep(1)
# e.send_keys(googleID)
# time.sleep(1)
# e.send_keys(Keys.ENTER)

# e = driver.find_element(By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
# time.sleep(1)
# e.send_keys(googlePW)
# time.sleep(1)
# e.send_keys(Keys.ENTER)

# driver.get('https://photos.google.com/')
# driver.implicitly_wait(5)
# time.sleep(5)

PROFILE = r'C:\remote-profile'              # 사용자 프로필 디렉토리
PORT = 9222                                 # Chrome 원격 디버깅을 위한 포트 번호

# Chrome 실행 파일의 경로 저장
cmd = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cmd += f' --user-data-dir="{PROFILE}"'	    # 사용자 데이터 디렉토리 지정
cmd += f' --remote-debugging-port={PORT}'  # 옵션을 사용하여 원격 디버깅 포트 지정
subprocess.Popen(cmd)	                    # Chrome 실행

# Chrome 인스턴스를 특정 디버깅 포트로 연결하여 디버깅
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('debuggerAddress', f'127.0.0.1:{PORT}')
driver = webdriver.Chrome(options=chrome_options)
time.sleep(4)
driver.get('https://photos.google.com/')
time.sleep(4)
# pyautogui.press('esc')
time.sleep(1)
try:
    driver.find_element(By.CSS_SELECTOR, "#glue-cookie-notification-bar-1 > button.glue-cookie-notification-bar__reject").click()
    time.sleep(4)
except:
    driver.get('https://photos.app.goo.gl/y2mM')
    time.sleep(4)
# driver.find_element(By.CSS_SELECTOR, "#body > div.main > div.hero.ng-scope > div.hero__content.css-parallax-ready > div.hero__content__main > div > div.hero__content__main__chapter__buttons > div: nth-child(2) > a").click()
driver.implicitly_wait(5)
#body > div.main > div.hero.ng-scope > div.hero__content.css-parallax-ready > div.hero__content__main > div > div.hero__content__main__chapter__buttons > div: nth-child(2) > a

e = driver.find_element(By.CSS_SELECTOR, "#identifierId")
time.sleep(1)
e.send_keys(googleID)
time.sleep(1)
e.send_keys(Keys.ENTER)

e = driver.find_element(By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
time.sleep(1)
e.send_keys(googlePW)
time.sleep(1)
e.send_keys(Keys.ENTER)

driver.get('https://photos.google.com/')
driver.implicitly_wait(5)
time.sleep(5)
