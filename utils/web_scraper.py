from typing import Optional

import lxml.html as html
from pandas import DataFrame
from requests import get

from config import URL_START, proxies, headers, URL_BASE
from utils.tender import Tender, Branch


class WebScraper:
    def __init__(self):
        self.tenders_list: list = []

    def parse_website(self, max_tenders: int = None) -> DataFrame:
        next_page = self.parse_webpage(URL_START)
        while next_page is not None:
            if max_tenders is not None:
                if max_tenders <= len(self.tenders_list):
                    self.tenders_list = self.tenders_list[:max_tenders]
                    break
            next_page = self.parse_webpage(next_page)
        return DataFrame.from_records(self.tenders_list)

    def parse_webpage(self, url: str) -> Optional[str]:
        next_page_ref: str
        parsed_body = html.fromstring(
            get(URL_BASE + url, timeout=30, proxies=proxies, headers = headers).text
        )
        next_page = parsed_body.xpath("//ul[@class='pagination']/li[@class='last']/a/@href")
        if len(next_page) != 0:
            next_page_ref = next_page[0]
        else:
            return None

        tenders = parsed_body.xpath("//article[@class='tender-row row']")
        for tender in tenders:
            td = Tender(
                number = tender.get('id'),
                link = tender.xpath(".//div[@class='tender-info']/a/@href")[0],
                dt_start = tender.xpath(".//time[@class='dtstart']")[0].text,
                dt_end = tender.xpath(".//time[@class='dtend']")[0].text,
                description = tender.xpath(".//div[@class='tender-info']/a")[0].text_content(),
                address = tender.xpath(".//div[@class='tender-address ']")[0].text_content(),
                region = tender.xpath(".//a[@class='tender__region-link']")[0].text,
                starting_price = tender_[0].text_content()
                if len(tender_ := tender.xpath(".//div[@class='starting-price__price starting-price--price']")) != 0 else "-",
                branches = [Branch(name = b.text) for b in tender.xpath(".//a[@class='list-branches__link']")]
            )

            self.tenders_list.append(td.asdict())
        return next_page_ref