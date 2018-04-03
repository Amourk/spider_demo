# from urllib.parse import urljoin
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

# 网页解析器
# from test import re


class HtmlParser:

    def parse(self, url, content, html_encode="utf-8"):
        if url is None or content is None:
            return

        soup = BeautifulSoup(content, "lxml")
        new_urls = self.new_get_urls(url, soup)
        new_data = self.get_new_data(url, soup)
        return new_urls, new_data



    # 从爬取这个的网页中提取新的url放入集合中
    def new_get_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile(r"/item/\w+"))

        for link in links:
            url_path = link["href"]
            new_url = urljoin(url, url_path)
            new_urls.add(new_url)

        return new_urls

    # 将网页的内容放入字典中
    def get_new_data(self, url, soup):
        data={"url":url}
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        data["title"] = title_node.get_text()
        summary_node = soup.find("div", class_="lemma-summary")
        data["summary"] = summary_node.get_text()
        return data



