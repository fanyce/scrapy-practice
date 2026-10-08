import base64
import re
import zlib

import scrapy


class XidianSpider(scrapy.Spider):
    name = "xidian"
    max_page = 3

    allowed_domains = ["job.xidian.edu.cn"]
    start_urls = ["https://job.xidian.edu.cn/campus"]

    def parse(self, response, page=1):
        print("CURRENT PAGE =", page)

        encoded = self.extract_encoded(response.text)

        if not encoded:
            self.logger.error("compressed payload not found")
            return

        html = self.decode_payload(encoded)
        selector = scrapy.Selector(text=html)

        # 当前页招聘列表
        for row in selector.css("ul.infoList")[:3]:
            title = row.css("li.span7 a::text").get()
            url = row.css("li.span7 a::attr(href)").get()
            publish_time = row.css("li.span4::text").get()

            print("LIST:", title, publish_time, url)

            yield response.follow(
                url,
                callback=self.parse_detail,
                cb_kwargs={
                    "title": title,
                    "publish_time": publish_time,
                },
            )

        # 已经到第3页，不再继续翻页
        if page >= self.max_page:
            return

        next_url = selector.css("li.next a::attr(href)").get()

        if next_url and not next_url.startswith("javascript:"):
            yield response.follow(
                next_url,
                callback=self.parse,
                cb_kwargs={
                    "page": page + 1,
                },
            )

    def parse_detail(self, response, title, publish_time):
        print("\n================ DETAIL ================")
        print("TITLE:", title)
        print("URL:", response.url)
        print("TIME:", publish_time)

        # 先观察详情页前 3000 个字符
        print(response.text[:3000])

    def extract_encoded(self, html):
        match = re.search(r'unzip\("([^"]+)"\)', html)

        if not match:
            return None

        return match.group(1)

    def decode_payload(self, encoded):
        compressed = base64.b64decode(encoded)
        data = zlib.decompress(compressed)

        data = data[25:]
        data = base64.b64decode(data)

        html = data.decode("utf-8")

        return html[35:]