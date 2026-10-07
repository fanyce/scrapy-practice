import scrapy


class XidianSpider(scrapy.Spider):
    name = "xidian"
    allowed_domains = ["job.xidian.edu.cn"]
    start_urls = ["https://job.xidian.edu.cn/campus"]

    def parse(self, response):
        self.logger.info("status=%s url=%s", response.status, response.url)
