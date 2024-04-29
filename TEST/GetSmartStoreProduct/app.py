from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import urllib.request
import time
import random
import os
import json

# web_driver.find_element(By.ID, "id")

# web_driver.find_element(By.NAME, "name")

# web_driver.find_element(By.XPATH, "xpath")

# web_driver.find_element(By.LINK_TEXT, "link text")

# web_driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")

# web_driver.find_element(By.TAG_NAME, "tag name")

# web_driver.find_element(By.CLASS_NAME, "class name")

# web_driver.find_element(By.CSS_SELECTOR, "css selector")



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome('chrome-win64/chrome.exe') # 구버전
# driver.get('https://instagram.com')

# # 자동화할때 젤중요(페이지 이동시 자주 필요)
# time.sleep(5)

# # 아이디 입력
# e = driver.find_elements(By.CLASS_NAME, "_aa4b")[0]
# e.send_keys('selenium')

# # 비번 입력
# e = driver.find_elements(By.CLASS_NAME, "_aa4b")[1]
# e.send_keys('selenium')
# e.send_keys(Keys.ENTER) #키보드 입력 구현

# # 페이지 이동시 Delay Time 필요
# time.sleep(3)

downLoadCmp = 0
downLoadCnt = 4
downLoadEnd = False
productDownStart = False

file_path = 'Json\\ProductList.json'
with open(file_path, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
json.dumps(json_data, indent=4)

# driver.get('https://smartstore.naver.com/kkubungestore')
# 전체상품
driver.get('https://smartstore.naver.com/kkubungestore/category/4541a09f254c432a8d8182651cda364e?cp=1')
driver.implicitly_wait(5)
# 최신등록순
e = driver.find_elements(By.CSS_SELECTOR, "div.wiPgcFH7Gk div._1jMHn1EJq2 ul li")[1].click()
# CSS_SELECTOR >> #id, .Class
# 전체상품에서 페이지 리스트 찾는다.
e = driver.find_elements(By.CSS_SELECTOR, "div#CategoryProducts ._1HJarNZHiI a")
# 맨 뒷 페이지가 나올때까지
while True:
    if e[len(e)-1].get_attribute("aria-hidden") == "false":
        e[len(e)-1].click()
        driver.implicitly_wait(5)
        e = driver.find_elements(By.CSS_SELECTOR, "div#CategoryProducts ._1HJarNZHiI a")
        print("Next Page >> ")
    else:
        break

while True:
    # 페이지 그룹의 페이지 갯수 가저오기
    pageCnt = driver.find_elements(By.CSS_SELECTOR, "div#CategoryProducts ._1HJarNZHiI a.UWN4IvaQza")
    num_e = len(pageCnt)

    # 페이지그룹의 마지막 페이지부터
    for i in range(num_e, 0, -1):

        if (downLoadEnd):
            print("Down Load End!!!")
            break

        pageCnt = driver.find_elements(By.CSS_SELECTOR, "div#CategoryProducts ._1HJarNZHiI a.UWN4IvaQza")
        pageCnt[i-1].click()
        print("Page Num : " + str(i-1))
        time.sleep(5)

        #############################################################################################
        # 각 페이지의 상품 리스트 가져오기
        #############################################################################################
        # 해당 페이지에서 제일 오래된 상품의 Url 취득 및 선택
        productList = driver.find_elements(By.CSS_SELECTOR, "#CategoryProducts ul.wOWfwtMC_3 li.flu7YgFW2k")
        productListCnt = len(productList) - 1
        i = productListCnt

        for i in range(productListCnt, 0, -1):

            # print("test i = " + str(i))
            productList = driver.find_elements(By.CSS_SELECTOR, "#CategoryProducts ul.wOWfwtMC_3 li.flu7YgFW2k")
            listName = productList[i].find_element(By.CSS_SELECTOR, "div._2kRKWS_t1E a strong._26YxgX-Nu5").text

            print("페이지 리스트 상품명 : " + listName)

            # 다운로드한 마지막 data
            dataLen = len(json_data['dataBackUp'])
            print("json File 가장 최신 상품명 : " + json_data['dataBackUp'][dataLen-1]['productName'])

            # 마지막 data와 Product Name 비교하여 다운로드 할지 말지 결정
            if (not productDownStart):
                if (dataLen > 0):
                    if (json_data['dataBackUp'][dataLen-1]['productName'] != listName):
                        productDownStart = False
                        continue
                    elif (productDownStart == False and json_data['dataBackUp'][dataLen-1]['productName'] == listName):
                        productDownStart = True
                        continue
                else:
                    productDownStart = True

            if (productDownStart):
                url = productList[i].find_element(By.CSS_SELECTOR, "div._2kRKWS_t1E a").get_attribute("href")
                print("제품url : "+url)
                productList[i].click()

                time.sleep(5)

                # 제품명 가져오기
                productName = driver.find_elements(By.CSS_SELECTOR, "div._1eddO7u4UC h3._22kNQuEXmb")[0].text
                #content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div._1eddO7u4UC > h3
                print("제품명 : " + productName)

                # 제품ID 가져오기
                productID = driver.find_elements(By.CSS_SELECTOR, "div._2E4i2Scsp4 table._1_UiXWHt__ tbody tr")[0].find_element(By.CSS_SELECTOR, "td.ABROiEshTD b").text
                print("제품ID : " + productID)

                # print("==============")
                # 현재 Path
                path = os.path.dirname(os.path.abspath(__file__))
                # 제품 ID로 Img 폴더 안에 폴더 만들기
                pathNew = path + "\\Img\\" + productID + "\\"
                # 제품 ID의 폴더가 없으면 다시 만들기
                if os.path.isdir(pathNew) == False:
                    os.mkdir(pathNew)

                print("저장 경로 : " + pathNew)
                # print("==============")

                # Tag 가져오기
                tag = driver.find_elements(By.CSS_SELECTOR, "ul._3Vox1DKZiA li._2RkVi-H2ze")
                # Tag 갯수
                TagCnt = len(tag)

                tagList = list()

                for n in range(0, TagCnt):
                    tagStr = driver.find_elements(By.CSS_SELECTOR, "ul._3Vox1DKZiA li._2RkVi-H2ze")[n].find_element(By.CSS_SELECTOR, "a._3SMi-TrYq2").text
                    print("Tag" + str(n) + " : " + tagStr)
                    tagList.insert(n, tagStr)

                # print(tagList)

                # Image
                smallImg = driver.find_elements(By.CSS_SELECTOR, "div.bd_QL0fx ul.bd_2YVUb li.bd_2q-LL")
                smallImgCnt = len(smallImg)
                print("small Img Cnt = " + str(smallImgCnt))

                if (smallImgCnt > 0):
                    for n in range(0, smallImgCnt):
                        smallImg[n].click()
                        driver.implicitly_wait(5)
                        # Image src 가져오기
                        e = driver.find_element(By.CSS_SELECTOR, "div._3rXou9cfw2 div.bd_23RhM div.bd_1uFKu img").get_attribute("src")
                        # Image 저장
                        urllib.request.urlretrieve(e, pathNew + productID + '_' + str(n) + '.jpg')
                        time.sleep(3)
                else:
                    e = driver.find_element(By.CSS_SELECTOR, "div._3rXou9cfw2 div.bd_23RhM div.bd_1uFKu img").get_attribute("src")
                    # Image 저장
                    urllib.request.urlretrieve(e, pathNew + productID + '.jpg')
                    smallImgCnt = 1
                    time.sleep(3)

                #############################################################################################
                # 상품 정보 Json 저장
                #############################################################################################
                downLoad_date = datetime.today().strftime("%Y%m%d%H%M%S")
                new_data = {
                    "produntID": productID,
                    "productName": productName,
                    "imgSavePath": pathNew,
                    "url": url,
                    "imgCnt": smallImgCnt,
                    "downLoadDate": downLoad_date,
                    "tag" : tagList
                }

                json_data['dataBackUp'].append(new_data)

                with open(file_path, 'w', encoding='utf-8') as outfile:
                    json.dump(json_data, outfile, indent=4, ensure_ascii=False)

                driver.back()
                time.sleep(5)

                downLoadCmp = downLoadCmp + 1
                print("Down Load Succes : " + str(downLoadCmp))
                if (downLoadCmp >= downLoadCnt):
                    downLoadEnd = True
                    break

    # 이전 페이지 버튼이 있으면 클릭하고 다시 페이지 선택 반복
    e = driver.find_elements(By.CSS_SELECTOR, "div#CategoryProducts ._1HJarNZHiI a._2PB8-gs2tG")
    if e[0].get_attribute("aria-hidden") == "false":
       e[0].click()
       print("Befor Page << ")
       time.sleep(5)
    else:
       break

print("End!!!")


