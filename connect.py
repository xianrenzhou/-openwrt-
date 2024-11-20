import requests
username = "" #学号
password = "" #姓名
session = requests.Session()
try:
    response = session.get("http://10.3.8.216", timeout=5)
except requests.exceptions.Timeout:
    print("Timeout error")
    exit()
except Exception as e:
    print(f"Error: {e}")
    exit()

cookies = str(session.cookies).split(" ")[1]
print(cookies)
url = "http://10.3.8.216/login"

payload = f'user={username}&pass={password}'
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': cookies,
  'Origin': 'http://10.3.8.216',
  'Referer': 'http://10.3.8.216/index',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
