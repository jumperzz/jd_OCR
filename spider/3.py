from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context #默认不需要校验证书验证

base_url = 'https://www.12306.cn/index/'

response = request.urlopen(base_url)
print(response.read().decode('utf-8'))