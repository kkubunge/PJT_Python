import requests

url = 'http://www.alie.kr/api/shoturl.siso'
payload = {
    'customer_id': 'kkubunge',
    'partner_api_id': '0D40392FF26C41BF37FAF7BEC230DC02',
    'org_url': 'https://smartstore.naver.com/kkubungestore/products/10020288743'
}

response = requests.post(url, data=payload)

print(response.text)
