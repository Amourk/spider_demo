import urllib.request
import requests

url = "https://baike.baidu.com/item/Android"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}

html = requests.get(url, headers=headers)
html.encoding = 'utf-8'
print(html.text)

# data = {"url":"sdasdas"}
# data["title"]="sdasfasfdsgf"
# print(data)