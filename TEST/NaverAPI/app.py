import urllib
import urllib.request
import urllib.parse
import bcrypt  # pip install bcrypt
import pybase64  # pip install pybase64
import time
import requests
import urllib3
from datetime import datetime, timedelta

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app_ID = "28HXQytrZEW9EuOsCUBzmJ"
app_Secret = "$2a$04$k7NoYJhsY8cpFhnDZICMRO"

def get_token(client_id, clientSecret, type_="SELF"):
    # 3초전 timestamp
    timestamp = str(int((time.time()-3) * 1000))
    # 밑줄로 연결하여 password 생성
    password = client_id + "_" + timestamp
    # bcrypt 해싱
    hashed = bcrypt.hashpw(password.encode('utf-8'), clientSecret.encode('utf-8'))
    # base64 인코딩
    client_secret_sign = pybase64.standard_b64encode(hashed).decode('utf-8')

    print(pybase64.standard_b64encode(hashed).decode('utf-8'))

    headers = {"content-type": "application/x-www-form-urlencoded"}
    data_ = {
        "client_id": client_id,
        "timestamp": timestamp,
        "grant_type": "client_credentials",
        "client_secret_sign": client_secret_sign,
        "type": type_
    }
    query = urllib.parse.urlencode(data_)
    print(query)
    oauth_url = 'https://api.commerce.naver.com/external/v1/oauth2/token?' + query
    response = requests.post(url=oauth_url, headers=headers, verify=False)
    response_data = response.json()

    if 'access_token' in response_data:
        return response_data['access_token']

    else:
        print(response_data)
        print("토큰 요청 실패")
        time.sleep(1)

def get_Product_data(ProductNo, token):
    # API : https://apicenter.commerce.naver.com/ko/basic/commerce-api#tag/%EC%83%81%ED%92%88/operation/readChannelProduct.product

    oauth_url = "https://api.commerce.naver.com/external/v2/products/channel-products/" + ProductNo
    headers = {'Authorization': token}

    response = requests.get(url=oauth_url, headers=headers, verify=False)
    response_data = response.json()
    return response_data

def get_Product_list(token):
    # API : https://apicenter.commerce.naver.com/ko/basic/commerce-api#tag/%EC%83%81%ED%92%88-%EB%AA%A9%EB%A1%9D

    payload = "{\"searchKeywordType\":\"\",\"channelProductNos\":[],\"originProductNos\":[],\"sellerManagementCode\":\"\",\"productStatusTypes\":[\"SALE\"],\"page\":1,\"size\":500,\"orderType\":\"NO\",\"periodType\":\"PROD_REG_DAY\",\"fromDate\":\"2024-01-01\",\"toDate\":\"2024-04-09\"}"

    oauth_url = "https://api.commerce.naver.com/external/v1/products/search"
    headers = {
        'Authorization': token,
        'content-type': "application/json"
    }
    response = requests.post(url=oauth_url, data=payload, headers=headers, verify=False)
    response_data = response.json()
    return response_data


def get_new_order_list(token):

    headers = {'Authorization': token}
    oauth_url = 'https://api.commerce.naver.com/external/v1/pay-order/seller/product-orders/last-changed-statuses'

    now = datetime.now()
    before_date = now - timedelta(hours=23)  # 23시간전
    from_date = before_date.strftime("%Y-%m-%dT%H:%M:%S.000+09:00")
    to_date = now.strftime("%Y-%m-%dT%H:%M:%S.000+09:00")
    # before_date = now - timedelta(hours=3) #3시간전
    # before_date = now - timedelta(seconds=10) #10초전
    # before_date = now - timedelta(minutes=10) #10분전


    print("before : " + from_date + " ~ " + to_date)
    # Example: lastChangedFrom=2022-04-11T15:21:44.000+09:00

    params = {
        'lastChangedFrom': from_date,  # 조회 시작 일시
        'lastChangedTo': to_date,  # 24시간 기준으로 설정해야 함...
            # 'lastChangedType': 'PAYED', #최종변경구분(PAYED : 결제완료, DISPATCHED : 발송처리)
    }

    response = requests.get(url=oauth_url, headers=headers, params=params, verify=False)
    # response = requests.get(url=new_oauth_url, headers=headers, verify=False)
    print(response)
    print("status code :", response.status_code)
    print("status url :", response.url)
    response_data = response.json()

    if 'data' not in response_data:  # 조회된 정보가 없을 경우 data키 없음
        print('주문 내역 없음')
    else:
        data_list = response_data['data']['lastChangeStatuses']
        for data in data_list:
            print('주문 내역 있음 : ' + str(response_data['data']['count']))

    return response_data







token = get_token(client_id=app_ID, clientSecret=app_Secret)
print(f'발급된 토큰 : ', token)
print("============================================")


# product_data = get_Product_data("10143803054", token)
# print(product_data)


# product_List = get_Product_list(token)
# print(product_List)
# print("============================================")
# print(str(len(product_List["contents"])))

order_List = get_new_order_list(token)
print(order_List)




