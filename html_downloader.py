import urllib.request
import requests

# 爬虫下载器
class HtmlDownLoader(object):
    def downloader(self, url):
        if url is None:
            return None

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}
        html = requests.get(url, headers=headers)
        html.encoding = 'utf-8'


        # response = urllib.request.urlopen(url)
        if html.status_code != 200:
            return None

        return html.text
