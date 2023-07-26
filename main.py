import os

import bs4
import requests
from requests_html import HTMLSession
import json
from typing import IO
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import uncurl
from dotenv import load_dotenv


class FormFiller:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)

    def fill_out_form(self):
        self.driver.get(FORM_URL)


class ZillowDataGetter:
    def __init__(self):
        self.session = HTMLSession()
        self.url = "https://www.zillow.com/search/GetSearchPageState.htm"
        self.prices = []
        self.addresses = []
        self.urls = []
        self.raw_params = '{"mapBounds":{"west":-78.719592,"east":-78.388793,"south":35.869345,"north":36.09583},' \
                     '"isMapVisible":false,' \
                     '"filterState":{"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},' \
                     '"cmsn":{"value":false},"auc":{"value":false},"fr":{"value":true},"ah":{"value":true}},' \
                     '"isListVisible":true,' \
                     '"pagination":{"currentPage":1}}'
        self.page_text = None
        self.json_data = self.get_zillow_data()

    def get_zillow_data(self, pages):
        """

        :param pages: Number of pages of JSON data to parse
        :return:
        """

        dict_params = json.loads(self.raw_params)

        for page in range(1, pages+1):
            time.sleep(5)
            dict_params["pagination"]["currentPage"] = page
            sqs = json.dumps(dict_params)

            zillow_response = self.session.get(self.url,
                                          params={"searchQueryState": sqs,
                                                  "wants": '{"cat1":["listResults"]}'},
                                          headers={
                                              "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                              "accept-language": "en-US,en;q=0.9",
                                              "authority": "www.zillow.com",
                                              "cache-control": "no-cache",
                                              "dnt": "1",
                                              "pragma": "no-cache",
                                              "referer": "https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A36.083312%2C%22east%22%3A-78.388787%2C%22south%22%3A35.869345%2C%22west%22%3A-78.719592%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForRent%22%3A%7B%22value%22%3Atrue%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A8%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A55006%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A1%7D%7D&wants={%22cat1%22:[%22listResults%22]}",
                                              "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
                                              "sec-ch-ua-mobile": "?0",
                                              "sec-ch-ua-platform": "\"Windows\"",
                                              "sec-fetch-dest": "document",
                                              "sec-fetch-mode": "navigate",
                                              "sec-fetch-site": "same-origin",
                                              "upgrade-insecure-requests": "1",
                                              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
                                          },
                                          cookies={
                                              "AWSALB": "T1P1cBmoHU/ACXErvhop8lSmdcxf4PI4A8VDhQqBUnEGzSka7h18Lt8au5XNzBj4zpk7NbgnyEdq6GBIVKWP0OXTC9U6GNONiDSjbOJ8pASLpURk1yzCFCxJ8UnS",
                                              "AWSALBCORS": "T1P1cBmoHU/ACXErvhop8lSmdcxf4PI4A8VDhQqBUnEGzSka7h18Lt8au5XNzBj4zpk7NbgnyEdq6GBIVKWP0OXTC9U6GNONiDSjbOJ8pASLpURk1yzCFCxJ8UnS",
                                              "JSESSIONID": "4DB9E05DEA644FCB5025365434F651DF",
                                              "_px3": "75c51a489f5afbb6c47b914c34ff154fd1a97a71771533f05cd7035879b0ce6c:hoeWM6S0dmIiOf9tP1AyLcOylCQT2CKvZAfVR6Ill2UMzjLP6Vpt2GKmA0FcWFqSsOk5GYTR0b7p4cZMbQEMjQ==:1000:jJmiYyttRLm5uAz5GiHekhvzJAV9+DwX/70zb4jcEohr5ztL6ftUW4xJnBUvheeU60e40UgUFu/aJnxnRAcvJFlnJbok8YUrXUdIsTZZN+aUVDylkB+1J7ntjbXstBp4VCuy1wahOj9m6R7zIdolF96su/cPvCILx+5hwVrjVAOXMVeUrg3yPwtNEa2JITdZul2EToElB8CMxkpliAuXoQ==",
                                              "_pxff_bsco": "1",
                                              "_pxff_cc": "U2FtZVNpdGU9TGF4Ow==",
                                              "_pxff_ccc": "1",
                                              "_pxff_cfp": "1",
                                              "_pxff_fp": "1",
                                              "_pxff_rf": "1",
                                              "_pxvid": "547a0727-2b00-11ee-9b4b-e9d718784bcf",
                                              "pxcts": "547a1d9d-2b00-11ee-9b4b-4d5a4a726b55",
                                              "search": "6|1692891111413%7Crect%3D36.083312%252C-78.388787%252C35.869345%252C-78.719592%26rid%3D55006%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26excludeNullAvailabilityDates%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%09%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09",
                                              "x-amz-continuous-deployment-state": "AYABePPOdfBdgPyfaAT6b0xTh08APgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADGOMrG6H3RoVa+8UjgAw4xgR4RWf6IhmRODGe9bfUZFdIcZYT8OdmX4DoSp7gML2PolWhXBB2z25Q29JMikyAgAAAAAMAAQAAAAAAAAAAAAAAAAAACGMkpgPlFROUoO3rmHJioD%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxff9VAUVL0TU1o2Q%2FhCcEz%2Fg48c4NFwlTlRGjO48c4NFwlTlRGjA==",
                                              "zg_anonymous_id": "%220a888c77-0441-41ec-8627-eba6dbe3e90c%22",
                                              "zgsession": "1|691c9528-a4e2-46e0-a414-2730513eca9d",
                                              "zguid": "24|%247a3a9caf-714d-4fe5-a574-56ed9a8101a5",
                                              "zjs_anonymous_id": "%224668c34f-19de-4a17-a92a-00b39dcf8a56%22",
                                              "zjs_user_id": "null"
                                              })
            self.page_text = zillow_response.text
            data = zillow_response.json()
            results = data["cat1"]["searchResults"]["listResults"]
            return results

    def process_data(self, results: list[dict]) -> None:
        """takes a subset of JSON data as an argument as mutates the prices, addresses, and urls lists."""
        i = 0
        for result in self.json_data:
            i += 1
            listing_url = f'https://www.zillow.com{result["detailUrl"]}'
            if "units" in [k for k in result.keys()]:
                units = result["units"]
                for unit in units:
                    unit_price = unit["price"]
                    unit_address = result['address']
                    self.prices.append(unit_price)
                    self.addresses.append(unit_address)
                    self.urls.append(listing_url)
            else:
                unit_price = result["price"]
                unit_address = result["address"]
                self.prices.append(unit_price)
                self.addresses.append(unit_address)
                self.urls.append(listing_url)
        print(i)


load_dotenv("env.env")
FORM_URL = os.environ.get("FORM_URL")


zillow_scraper = ZillowDataGetter()
zillow_scraper.process_data(zillow_scraper.json_data, 1)
print(zillow_scraper.prices, zillow_scraper.addresses, zillow_scraper.urls)
# get_zillow_data()
# data_processing(results)
# print(prices, len(prices))
# print(addresses, len(addresses))
# print(urls, len(urls))
# FormFiller()
