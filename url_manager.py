
# 爬虫url管理器
class UrlManager:
    # 初始化两个set用于存储url
    def __init__(self):
        # 存储新的， 没有用过的url
        self.new_urls = set()
        # 存储已经用过的url
        self.use_urls = set()

    # 添加新的url到new_urls
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.use_urls:
            self.new_urls.add(url)

    # 将爬取到的urls集合依次放入new-urls中进行再次爬取
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断new_urls中是否还有新的url可以爬取数据
    def has_new_url(self):
        return len(self.new_urls) > 0

    # 取出new_urls中的第一个url进行爬取数据
    def get_new_url(self):
        temp_url = self.new_urls.pop()
        self.use_urls.add(temp_url)
        return temp_url
