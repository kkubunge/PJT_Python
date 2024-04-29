from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import urllib.request
import time
import random
import os
import json
import pyautogui
from pathlib import Path
import pyperclip

def Instar_LogIn(id, pw):

    e = driver.find_elements(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
    time.sleep(1)
    e[0].send_keys(instarID)
    time.sleep(1)

    e = driver.find_elements(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
    e[0].send_keys(instarPW)
    time.sleep(1)
    e[0].send_keys(Keys.ENTER)
    driver.implicitly_wait(10)

    # 로그인 정보저장>나중에하기
    e = driver.find_element(By.CSS_SELECTOR, "div.x1gryazu section > main > div > div > div > div > div.x1i10hfl.xjqpnuy").click()
    time.sleep(3)

    # 알림 > 나중에하기
    e = driver.find_element(By.CSS_SELECTOR, 'div.x7r02ix.xf1ldfh > div > div > div._a9-z > button._a9--._ap36._a9_1').click()
    time.sleep(3)

    return

def Instar_Reple():

    shortUrl = "상품 상세페이지 👉👉👉👉 TRSET "
    pyperclip.copy(shortUrl)

    #  프로필 클릭
    e = driver.find_element(By.CSS_SELECTOR, 'div.x1iyjqo2.xh8yej3 > div:nth-child(8) > div > span > div > a > div > div:nth-child(1) > div > div > span > img').click()
    time.sleep(3)
    # 1번째 게시물 클릭
    e = driver.find_element(By.CSS_SELECTOR, 'main > div > div:nth-child(4) > div > div:nth-child(1) > div:nth-child(1) > a > div._aagu > div._aagw').click()
    time.sleep(3)
    # 사진 더블클릭
    e = driver.find_element(By.CSS_SELECTOR, 'div.x9f619 > div > div > div > ul > li:nth-child(2) > div > div > div:nth-child(1) > div > div._aagw')
    ActionChains(driver)\
        .double_click(e)\
        .perform()
    time.sleep(3)
    # 댓글 클릭
    e = driver.find_element(By.CSS_SELECTOR, 'form > div > textarea').click()
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'v')

    return

def Instar_ContentsUpload(Cnt):

    for i in range(0, Cnt):
        # 만들기 클릭
        e = driver.find_element(By.CSS_SELECTOR, 'div.x1iyjqo2.xh8yej3 > div:nth-child(7) > div > span > div > a > div > div:nth-child(1) > div > div > svg').click()
        time.sleep(3)

        # 컴퓨터에서 선택
        e = driver.find_element(By.CSS_SELECTOR, 'div.xdl72j9.x1cwzgcd > div.x6s0dn4.xh8yej3 > div > div > div.x9f619.x1nhvcw1 > div > button').click()
        time.sleep(3)

        file_Path = ".\\Img\\8152749387"
        file_Img = "8152749387_0.jpg"
        file_Img1 = "8152749387_1.jpg"
        file_Img2 = "8152749387_2.jpg"

        dir_path=Path.cwd()
        file_path=f"{dir_path}"+'\\Img\\8152749387'

        print("file path : "+file_path)

        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(3)

        file_ImgTotal = f"\"{file_Img}\" \"{file_Img1}\" \"{file_Img2}\""
        pyautogui.write(file_ImgTotal)
        pyautogui.press('enter')
        time.sleep(3)

        # 사진 추가 후 다음 클릭
        e = driver.find_element(By.CSS_SELECTOR, 'div._ap97 > div > div > div > div._ac7b._ac7d > div > div').click()
        time.sleep(3)

        # 필터 조정 없이 다음 클릭
        e = driver.find_element(By.CSS_SELECTOR, 'div._ap97 > div > div > div > div._ac7b._ac7d > div > div').click()
        time.sleep(3)

        # 게시물 문구 입력
        e = driver.find_element(By.CSS_SELECTOR, 'div.xhk4uv > div > div > div > div._ac2p > div:nth-child(2)').click()
        time.sleep(1)
        pyautogui.write("TEST!!!!!!!!")
        time.sleep(3)

        # 공유하기 클릭
        e = driver.find_element(By.CSS_SELECTOR, 'div._ap97 > div > div > div > div._ac7b._ac7d > div > div').click()
        time.sleep(3)

        errorCnt = 0
        while 1:
            e = driver.find_element(By.CSS_SELECTOR, 'div.xdl72j9 > div.x6s0dn4 > div > div:nth-child(2) > div > span').text
            if (e == '게시물이 공유되었습니다.'):
                time.sleep(1)
                pyautogui.press('esc')
                driver.implicitly_wait(10)
                ret = True
                break
            else:
                time.sleep(3)
                errorCnt = errorCnt + 1

            # 3분동안 업로드가 안되면 ...
            if (errorCnt > 60):
                print("FAIL!!!!")
                ret = False
                break

        if (ret == False):
            break
    return

def Instar_ContentsLike(Cnt):

    ret = False
    likeCnt = 0
    oldContents = False

    # 좌측 메뉴 홈 클릭
    driver.find_element(By.CSS_SELECTOR, 'div.x1iyjqo2.xh8yej3 > div:nth-child(1) > div > span > div > a > div > div:nth-child(1) > div > div > svg').click()
    time.sleep(3)

    for i in range(0, Cnt):

        contents = driver.find_elements(By.CSS_SELECTOR, "article")
        # contents 갯수
        contentsCnt = len(contents)
        print("contentsCnt : " + str(contentsCnt))

        for y in range(0, contentsCnt):

            contentsType = ""
            try:
                # 광고
                contentsType = contents[y].find_element(By.CSS_SELECTOR, "div.x9f619 > div > div:nth-child(2) > span > div > span ").text
                print(contentsType)
                continue
            except:
                try:
                    # 추천 게시글
                    contentsType = contents[y].find_element(By.CSS_SELECTOR, "div > div:nth-child(1) > div:nth-child(3) > div").text
                    print(contentsType)
                    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div > div > div.xvbhtw8 > div > a > span').click()
                    oldContents = True
                    time.sleep(3)
                    continue
                except:
                    try:
                        likeChk = contents[y].find_element(By.CSS_SELECTOR, "section.x6s0dn4 > div.x78zum5 > span.xp7jhwk > div > div > span > svg").get_attribute("aria-label")
                        print(likeChk)
                    except:
                        print("???")

                if (likeChk == "좋아요"):
                    print("if (likeChk == 좋아요):")
                    contents[y].find_element(By.CSS_SELECTOR, "section.x6s0dn4 > div.x78zum5 > span.xp7jhwk > div > div").click()
                    time.sleep(3)
                    contents[y].find_element(By.CSS_SELECTOR, "section.x6s0dn4 > div.x78zum5 > span.xp7jhwk > div > div").click()
                    # sectionList = contents[y].find_elements(By.CSS_SELECTOR, "section.x6s0dn4 > div.x78zum5 > span.xp7jhwk > div")
                    # print(len(sectionList))
                    # sectionList[0].click()
                    time.sleep(3)
                    likeCnt += 1
                elif (likeChk == "좋아요 취소" and y == 0 and oldContents == False):
                    print("elif (likeChk == 좋아요 취소):")
                    # 첫 게시글에 좋아요가 클릭되어 있으면 이전 게시글으로 넘어감
                    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div > div > div.xvbhtw8 > div > a > span').click()
                    oldContents = True
                    time.sleep(3)

                if (likeCnt >= Cnt):
                    ret = True
                    break

        if (likeCnt >= Cnt):
            ret = True
            break
        else:
            ret = False
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(3)

    return ret

def Instar_Follow(Cnt):

    ret = False
    followCnt = 0

    # 좌측 메뉴 홈 클릭
    driver.find_element(By.CSS_SELECTOR, 'div.x1iyjqo2.xh8yej3 > div:nth-child(1) > div > span > div > a > div > div:nth-child(1) > div > div > svg').click()
    time.sleep(3)

    for i in range(0, Cnt):

        contents = driver.find_elements(By.CSS_SELECTOR, "article")
        # contents 갯수
        contentsCnt = len(contents)
        print("contentsCnt : " + str(contentsCnt))
        contentsType = ""

        for y in range(0, contentsCnt):

            try:
                # 추천 게시글
                contentsType = contents[y].find_element(By.CSS_SELECTOR, "div > div:nth-child(1) > div:nth-child(3) > div").text
                print(contentsType)

                if (contentsType == "팔로우"):
                    contents[y].find_element(By.CSS_SELECTOR, "div > div:nth-child(1) > div:nth-child(3) > div").click()
                    followCnt += 1
                    time.sleep(3)
            except:
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                continue

        if (followCnt >= Cnt):
            ret = True
            break
        else:
            ret = False
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(3)

    return ret
# 스크롤
# driver.execute_script("window.scrollTo(0,500);")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# driver.execute_script("return document.body.scrollHeight")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.instagram.com/')
driver.implicitly_wait(5)

instarID = "kkubunge._.store"
instarPW = "yoo!7212"
Instar_LogIn(instarID, instarPW)
time.sleep(3)
# Instar_ContentsUpload(2)
# time.sleep(3)
# Instar_ContentsLike(3)
# time.sleep(3)
# Instar_Follow(5)
Instar_Reple()
time.sleep(3)