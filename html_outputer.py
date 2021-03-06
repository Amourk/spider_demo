
# 应用器（输出爬取的结果）
import time


class HtmlOutPuter:

    # 初始化一个datas列表
    def __init__(self):
        self.datas = []

    # 添加爬取的内容放入datas中
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 用一个网页输出爬取的全部内容
    def output_html(self):
        fout = open("output.html", "w", encoding="utf-8")
        fout.write("<html>")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data["url"])
            fout.write("<td>%s</td>" % data["title"])
            fout.write("<td>%s</td>" % data["summary"])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        # file_name = time.strftime("%Y-%m-%d_%H:%M:%S")
        # with open("out_%s.html" % file_name, "w") as f_out:
        #     f_out.write("<html>")
        #     f_out.write(r'<head>'
        #                 r'<link rel="stylesheet" '
        #                 r'href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" '
        #                 r'integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" '
        #                 r'crossorigin="anonymous"></head>')
        #     f_out.write("<body>")
        #     f_out.write(r'<table class="table table-bordered table-hover">')
        #
        #     item_css = ['active', 'success', 'warning', 'info']
        #     for data in self.datas:
        #         index = self.datas.index(data) % len(item_css)
        #         f_out.write(r'<tr class="'+item_css[index]+r'">')
        #         f_out.write('<td>%s</td>' % data["url"])
        #         f_out.write('<td>%s</td>' % data["title"])
        #         f_out.write('<td>%s</td>' % data["summary"])
        #         f_out.write("</tr>")
        #
        #     f_out.write("</table>")
        #     f_out.write("</body>")
        #     f_out.write("</html>")

