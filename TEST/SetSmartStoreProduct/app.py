from bs4 import BeautifulSoup
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
import requests
from collections import Counter


def Get_CategoryID_Search(keyword):

    headers = {
        'authority': 'search.shopping.naver.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'NNB=D3SUWNPSZBMWI; SHP_BUCKET_ID=7; NSCS=1; ASID=77c561820000018829e0cf670000004b; _ga_GDZF0H5BMH=GS1.1.1685580047.1.1.1685581183.60.0.0; autocomplete=use; NV_WETR_LOCATION_RGN_M="MDkxNDAxMDQ="; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDAxMDQ="; nx_ssl=2; _ga_6Z6DP60WFK=GS1.2.1688975956.1.0.1688975956.60.0.0; nid_inf=-1407962044; NID_AUT=f8b+pILdyEifcBSTncJoLFl0+Whc/nOq54RnK6lJaAaDSQrTM8rP3X9oF+VA8xzm; NID_JKL=VmXShvyJ0iTA0i695jOR318HEyMvP9VR8/oyWhXy/bA=; _ga=GA1.2.1701136973.1690257791; ncpa=4536612|lkmruuxc|163b9bb0a6fc9e23efb55cdabd2a0d5b9a10fd9a|s_2da8726e5e7f6|8cb9022f652af4543fe1aa6064e8f833cfbd55e1; _ga_ZGQY5GH55D=GS1.1.1690562927.14.0.1690562927.0.0.0; NID_SES=AAABgnulEvEtdAPHwJ1sg5+M/yRdk1ri/MgNfPd4e9PNops4pWmCXi2zGt5QparrNe6gaGk0Cl/x3lR69AtOVPSsimjkZhuKpQNaQrkwMRUqBvRyom7MQ0DbubjA+mWSQ81NWinOJcvdLHxpR/VzaCZ9pJKX+hop9pFca0u8/VbGZfBSD/t7nIZ1GJxO5MD+gKvlF4MGLLh5PE5KmMORZJG3RJxqFnvsOKGQV4ekMjYP6cOLw4KBPpBllm6G+FCCRl8neP8XPK133d/K1tqd7rKNZeNHqthMVvZfE9vf97y6U7VDOMfsNjRRe8/XPyKuxgLiRYIeF8Z8spoiKOU6WtgVgrOJaPFnJ/u9yaPH9tbQxLrWBmCwRvNLJ7cb5s0jkRoA3E64bGYC+d/MlFtO04hT4xaJhhMbyeVAK9NwS/Z+mLXUnLSEMfdi+PfxB+SaRs6joH6TZfjbmrf67kWDwRpr60AVemusvpk/HdfyaSd6k0rTp4yf9GEP40H919frAVq4eblKLYKBLPMIKqy16LUt/Xk=; spage_uid=',
        'logic': 'PART',
        'referer': 'https://search.shopping.naver.com/search/all?query=%EC%98%A4%EB%8B%88%EC%B8%A0%EC%B9%B4%ED%83%80%EC%9D%B4%EA%B1%B0&cat_id=&frm=NVSHATC',
        'sbth': 'b77ad4005ee821024462d4b57e59d24e95ccc7062f65af77e4baf2a0c70a1c6677c58d9032794b7a0f06ee8fd74bcdde',
        'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="114"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Whale";v="3.21.192.18", "Not-A.Brand";v="8.0.0.0", "Chromium";v="114.0.5735.138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.18 Safari/537.36',
    }
    params = {
        'eq': '',
        'frm': 'NVSHATC',
        'iq': '',
        'origQuery': keyword,
        'pagingIndex': '1',
        'pagingSize': '100',
        'productSet': 'total',
        'query': keyword,
        'sort': 'rel',
        'viewType': 'list',
        'xq': '',
    }

    response = requests.get(
        'https://search.shopping.naver.com/api/search/all', params=params, headers=headers)
    result = json.loads(response.text)

    product_data = result['shoppingResult']['products']
    sameCnt = 0
    noSameCnt = 0
    cnt = len(product_data)

    json_data = [{
        'name': "",
        'category': "",
        'price': 0,
    }]

    for product in product_data:
        name = product['productTitle']
        price = product['price']
        categoryID = product['category4Id']
        if (categoryID == ""):
            categoryID = product['category3Id']
            if (categoryID == ""):
                categoryID = product['category2Id']
                if (categoryID == ""):
                    categoryID = product['categoryId']
        product_dict = {
            'name': name,
            'category': categoryID,
            'price': price,
        }
        # print(product_dict)
        json_data.append(product_dict)


    # print(json.dumps(json_data, indent=4, ensure_ascii=False))

    category_counts = Counter(elem['category'] for elem in json_data)
    duplicates = [category for category, count in category_counts.items() if count > 1]

    # for category in duplicates:
    #     print(f'duplicate category {category}: {category_counts[category]}')

    max_category = max(category_counts, key=category_counts.get)
    # print(f'The category with the most count is {max_category} with a count of {category_counts[max_category]}')

    return max_category


# 쇼핑 추천 키워드
def Get_ProductName_Search(search_word):

    headers = {
        'authority': 'search.shopping.naver.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'NNB=D3SUWNPSZBMWI; SHP_BUCKET_ID=7; NSCS=1; ASID=77c561820000018829e0cf670000004b; _ga_GDZF0H5BMH=GS1.1.1685580047.1.1.1685581183.60.0.0; autocomplete=use; NV_WETR_LOCATION_RGN_M="MDkxNDAxMDQ="; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDAxMDQ="; nx_ssl=2; _ga_6Z6DP60WFK=GS1.2.1688975956.1.0.1688975956.60.0.0; nid_inf=-1407962044; NID_AUT=f8b+pILdyEifcBSTncJoLFl0+Whc/nOq54RnK6lJaAaDSQrTM8rP3X9oF+VA8xzm; NID_JKL=VmXShvyJ0iTA0i695jOR318HEyMvP9VR8/oyWhXy/bA=; _ga=GA1.2.1701136973.1690257791; ncpa=4536612|lkmruuxc|163b9bb0a6fc9e23efb55cdabd2a0d5b9a10fd9a|s_2da8726e5e7f6|8cb9022f652af4543fe1aa6064e8f833cfbd55e1; _ga_ZGQY5GH55D=GS1.1.1690562927.14.0.1690562927.0.0.0; NID_SES=AAABgnulEvEtdAPHwJ1sg5+M/yRdk1ri/MgNfPd4e9PNops4pWmCXi2zGt5QparrNe6gaGk0Cl/x3lR69AtOVPSsimjkZhuKpQNaQrkwMRUqBvRyom7MQ0DbubjA+mWSQ81NWinOJcvdLHxpR/VzaCZ9pJKX+hop9pFca0u8/VbGZfBSD/t7nIZ1GJxO5MD+gKvlF4MGLLh5PE5KmMORZJG3RJxqFnvsOKGQV4ekMjYP6cOLw4KBPpBllm6G+FCCRl8neP8XPK133d/K1tqd7rKNZeNHqthMVvZfE9vf97y6U7VDOMfsNjRRe8/XPyKuxgLiRYIeF8Z8spoiKOU6WtgVgrOJaPFnJ/u9yaPH9tbQxLrWBmCwRvNLJ7cb5s0jkRoA3E64bGYC+d/MlFtO04hT4xaJhhMbyeVAK9NwS/Z+mLXUnLSEMfdi+PfxB+SaRs6joH6TZfjbmrf67kWDwRpr60AVemusvpk/HdfyaSd6k0rTp4yf9GEP40H919frAVq4eblKLYKBLPMIKqy16LUt/Xk=; spage_uid=',
        'logic': 'PART',
        'referer': 'https://search.shopping.naver.com/search/all?query=%EC%98%A4%EB%8B%88%EC%B8%A0%EC%B9%B4%ED%83%80%EC%9D%B4%EA%B1%B0&cat_id=&frm=NVSHATC',
        'sbth': 'b77ad4005ee821024462d4b57e59d24e95ccc7062f65af77e4baf2a0c70a1c6677c58d9032794b7a0f06ee8fd74bcdde',
        'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="114"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Whale";v="3.21.192.18", "Not-A.Brand";v="8.0.0.0", "Chromium";v="114.0.5735.138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.18 Safari/537.36',
    }
    params = {
        'eq': '',
        'frm': 'NVSHATC',
        'iq': '',
        'origQuery': keyword,
        'pagingIndex': '1',
        'pagingSize': '100',
        'productSet': 'total',
        'query': keyword,
        'sort': 'rel',
        'viewType': 'list',
        'xq': '',
    }

    response = requests.get(
        'https://search.shopping.naver.com/api/search/all', params=params, headers=headers)
    result = json.loads(response.text)

    product_data = result['shoppingResult']['products']

    json_data = [{
        'name': ""
    }]

    for product in product_data:
        # name = product['productTitle']
        name = product['productName']
        str_chars = name.split()
        cnt = len(str_chars)
        for i in range(0, cnt):

            if (str_chars[i] != '-'):
                product_dict = {
                    'name': str_chars[i]
                }
                # print(product_dict)
                json_data.append(product_dict)

    # print(json.dumps(json_data, indent=4, ensure_ascii=False))

    name_counts = Counter(elem['name'] for elem in json_data)
    duplicates = [name for name, count in name_counts.items() if count > 1]

    # for name in duplicates:
    #     print(f'duplicate name {name}: {name_counts[name]}')

    max_name = max(name_counts, key=name_counts.get)
    # print(f'The category with the most count is {max_name} with a count of {name_counts[max_name]}')

    # 상위 목록 30개
    top_names = name_counts.most_common(30)
    # for name, count in top_names:
    #     print(f'Name: {name}, Count: {count}')

    # 하위 목록 30개
    # bottom_names = name_counts.most_common()[:-30-1:-1]
    # for name, count in bottom_names:
    #     print(f'Name: {name}, Count: {count}')

    return top_names


def Get_ProductTag_Search(search_word):

    headers = {
        'authority': 'search.shopping.naver.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'NNB=D3SUWNPSZBMWI; SHP_BUCKET_ID=7; NSCS=1; ASID=77c561820000018829e0cf670000004b; _ga_GDZF0H5BMH=GS1.1.1685580047.1.1.1685581183.60.0.0; autocomplete=use; NV_WETR_LOCATION_RGN_M="MDkxNDAxMDQ="; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDAxMDQ="; nx_ssl=2; _ga_6Z6DP60WFK=GS1.2.1688975956.1.0.1688975956.60.0.0; nid_inf=-1407962044; NID_AUT=f8b+pILdyEifcBSTncJoLFl0+Whc/nOq54RnK6lJaAaDSQrTM8rP3X9oF+VA8xzm; NID_JKL=VmXShvyJ0iTA0i695jOR318HEyMvP9VR8/oyWhXy/bA=; _ga=GA1.2.1701136973.1690257791; ncpa=4536612|lkmruuxc|163b9bb0a6fc9e23efb55cdabd2a0d5b9a10fd9a|s_2da8726e5e7f6|8cb9022f652af4543fe1aa6064e8f833cfbd55e1; _ga_ZGQY5GH55D=GS1.1.1690562927.14.0.1690562927.0.0.0; NID_SES=AAABgnulEvEtdAPHwJ1sg5+M/yRdk1ri/MgNfPd4e9PNops4pWmCXi2zGt5QparrNe6gaGk0Cl/x3lR69AtOVPSsimjkZhuKpQNaQrkwMRUqBvRyom7MQ0DbubjA+mWSQ81NWinOJcvdLHxpR/VzaCZ9pJKX+hop9pFca0u8/VbGZfBSD/t7nIZ1GJxO5MD+gKvlF4MGLLh5PE5KmMORZJG3RJxqFnvsOKGQV4ekMjYP6cOLw4KBPpBllm6G+FCCRl8neP8XPK133d/K1tqd7rKNZeNHqthMVvZfE9vf97y6U7VDOMfsNjRRe8/XPyKuxgLiRYIeF8Z8spoiKOU6WtgVgrOJaPFnJ/u9yaPH9tbQxLrWBmCwRvNLJ7cb5s0jkRoA3E64bGYC+d/MlFtO04hT4xaJhhMbyeVAK9NwS/Z+mLXUnLSEMfdi+PfxB+SaRs6joH6TZfjbmrf67kWDwRpr60AVemusvpk/HdfyaSd6k0rTp4yf9GEP40H919frAVq4eblKLYKBLPMIKqy16LUt/Xk=; spage_uid=',
        'logic': 'PART',
        'referer': 'https://search.shopping.naver.com/search/all?query=%EC%98%A4%EB%8B%88%EC%B8%A0%EC%B9%B4%ED%83%80%EC%9D%B4%EA%B1%B0&cat_id=&frm=NVSHATC',
        'sbth': 'b77ad4005ee821024462d4b57e59d24e95ccc7062f65af77e4baf2a0c70a1c6677c58d9032794b7a0f06ee8fd74bcdde',
        'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="114"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Whale";v="3.21.192.18", "Not-A.Brand";v="8.0.0.0", "Chromium";v="114.0.5735.138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.18 Safari/537.36',
    }
    params = {
        'eq': '',
        'frm': 'NVSHATC',
        'iq': '',
        'origQuery': keyword,
        'pagingIndex': '1',
        'pagingSize': '100',
        'productSet': 'total',
        'query': keyword,
        'sort': 'rel',
        'viewType': 'list',
        'xq': '',
    }

    response = requests.get(
        'https://search.shopping.naver.com/api/search/all', params=params, headers=headers)
    result = json.loads(response.text)

    product_data = result['shoppingResult']['products']

    json_data = [{
        'tag': ""
    }]

    for product in product_data:
        # name = product['productTitle']
        tag = product['manuTag']
        str_chars = tag.split(',')
        cnt = len(str_chars)
        for i in range(0, cnt):
            if (str_chars[i] !=""):
                product_dict = {
                    'tag': str_chars[i]
                }
                # print(product_dict)
                json_data.append(product_dict)

    # print(json.dumps(json_data, indent=4, ensure_ascii=False))

    tag_counts = Counter(elem['tag'] for elem in json_data)
    duplicates = [tag for tag, count in tag_counts.items() if count > 1]

    # for tag in duplicates:
    #     print(f'duplicate tag {tag}: {tag_counts[tag]}')

    max_tag = max(tag_counts, key=tag_counts.get)
    # print(f'The category with the most count is {max_tag} with a count of {tag_counts[max_tag]}')

    # 상위 목록 30개
    top_tags = tag_counts.most_common(30)
    # for tag, count in top_tags:
    #     print(f'tag: {tag}, Count: {count}')

    # 하위 목록 30개
    # bottom_tags = tag_counts.most_common()[:-30-1:-1]
    # for tag, count in bottom_tags:
    #     print(f'tag: {tag}, Count: {count}')

    return top_tags


keyword = "피에른 접이식 선반"
maxCategoryID = Get_CategoryID_Search(keyword)
print("maxCategoryID : " + str(maxCategoryID))

top_names = Get_ProductName_Search(keyword)
print("================ Product Name ====================")
print(top_names)

top_tags = Get_ProductTag_Search(keyword)
print("================ Product Tag ====================")
print(top_tags)
