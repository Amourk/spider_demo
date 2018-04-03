import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain:
    # 初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.download = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.out = html_outputer.HtmlOutPuter()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                html_content = self.download.downloader(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content, "utf-8")
                self.urls.add_new_urls(new_urls)
                self.out.collect_data(new_data)
                if count > 30:
                    break
                count = count + 1
            except Exception as e:
                print("craw failed!\n" + str(e))
        self.out.output_html()


if __name__ == '__main__':
    rootUrl = "http://baike.baidu.com/item/Android"
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)
