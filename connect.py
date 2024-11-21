# Define username and password
# 定义用户名和密码
username = ""  # 学号 (student number)
password = ""  # 密码 (password)

def get_auth_url():
    """
    Function to obtain the authentication URL by sending a request to a captive portal URL.
    通过向强制门户 URL 发送请求来获取认证 URL 的函数。
    """
    url = "http://captive.apple.com"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    try:
        # Parse the redirect URL from the response text
        # 从响应文本中解析重定向 URL
        redirect_url = response.text.split("url=")[1].split("'>")[0]
        # Send a POST request to the redirect URL to obtain the actual authentication URL
        # 发送 POST 请求到重定向 URL 以获取实际的认证 URL
        response = requests.post(redirect_url, headers=headers, allow_redirects=False)
        auth_url = response.headers['Location'].split("/index")[0]
    except Exception:
        # Fallback URL if parsing or request fails
        # 如果解析或请求失败，使用备用 URL
        auth_url = "http://10.3.8.216"
    print(auth_url)
    return auth_url

# Get the authentication URL
# 获取认证 URL
url = get_auth_url()
session = requests.Session()

try:
    # Try to connect to the authentication URL with a timeout of 5 seconds
    # 尝试连接认证 URL，超时时间为 5 秒
    response = session.get(url, timeout=5)
except requests.exceptions.Timeout:
    # Handle timeout exception
    # 处理超时异常
    print("Timeout error")
    exit()
except Exception as e:
    # Handle other exceptions
    # 处理其他异常
    print(f"Error: {e}")
    exit()

# Extract cookies from the session
# 从会话中提取 cookies
cookies = str(session.cookies).split(" ")[1]
print(cookies)

# Define the payload with username and password for login
# 定义包含用户名和密码的登录数据
payload = f'user={username}&pass={password}'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': cookies,
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

try:
    # Send a POST request to the login endpoint with the credentials
    # 使用凭据向登录端点发送 POST 请求
    response = requests.post(f"{url}/login", headers=headers, data=payload)
except Exception:
    # Handle unknown errors during the login request
    # 处理登录请求中的未知错误
    print("Unknown error")

# Print the response status code to indicate the result of the login attempt
# 打印响应状态码以指示登录尝试的结果
print(response.status_code)
