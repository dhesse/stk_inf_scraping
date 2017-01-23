# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from urlparse import urljoin

class StkInfGhSpider(scrapy.Spider):
    name = "stk_inf_gh"
    start_urls = (
        'https://dhesse.github.io/stk_inf_scraping/example.html',
    )

    def parse(self, response):
        """Extract all list items, follow all links unconditionally
        (which is potentially dangerous)."""
        soup = BeautifulSoup(response.text, 'lxml')
        # first extract links and yield it,
        # together with the URL that it's from
        for li in soup('li'):
            yield {'item': li.text,
                   'url': response.url}
