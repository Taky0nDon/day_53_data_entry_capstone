import json
import os
import time

import requests.exceptions
import selenium.webdriver.remote.webelement
from dotenv import load_dotenv
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

load_dotenv("env.env")
FORM_URL = os.environ.get("FORM_URL")


class FormFiller:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)
        self.driver.get(FORM_URL)
        self.input_elements = self.find_inputs()
        self.address_input = self.input_elements[0]
        self.price_input = self.input_elements[1]
        self.link_input = self.input_elements[2]
        self.submit_button = None
        self.wait = WebDriverWait(self.driver, 5)
    def find_inputs(self):
        relevant_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
        self.input_elements = relevant_inputs
        self.address_input = relevant_inputs[0]
        self.price_input = relevant_inputs[1]
        self.link_input = relevant_inputs[2]
        return relevant_inputs

    def fill_input(self, input_field_to_fill: selenium.webdriver.remote.webelement.WebElement, text_to_enter: str):
        input_field_to_fill.send_keys(text_to_enter)

    def submit(self):
        self.submit_button = self.driver.find_element(By.XPATH, "//*/span[text()='Submit']")
        self.submit_button.click()

    def get_next_form(self):
        link_to_next_form = self.driver.find_element(By.LINK_TEXT, "Submit another response")
        link_to_next_form.click()

    def wait_for_forms_to_be_interactable(self):
        self.wait.until(ec.element_to_be_clickable(self.link_input))



class ZillowDataGetter:
    def __init__(self):
        self.session = HTMLSession()
        self.url = "https://www.zillow.com/search/GetSearchPageState.htm"
        self.prices = []
        self.addresses = []
        self.urls = []
        self.raw_params = '{"mapBounds":{"west":-78.719592,"east":-78.388793,"south":35.869345,"north":36.09583},' \
                          '"isMapVisible":false,' \
                          '"filterState":{"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},' \
                          '"fore":{"value":false},' \
                          '"cmsn":{"value":false},"auc":{"value":false},"fr":{"value":true},"ah":{"value":true}},' \
                          '"isListVisible":true,' \
                          '"pagination":{"currentPage":1}}'
        self.page_text = None
        self.json_data = None

    def get_zillow_data(self, pages: int = 1) -> list[dict] | str:
        """

        :param pages: Number of pages of JSON data to parse
        :return: list of dict where each dict is a listing matching the query (dict_params, derived from
        self.raw_params)
        """

        dict_params = json.loads(self.raw_params)
        results = "GET request failed."
        final_results = []
        for page in range(1, pages + 1):
            time.sleep(2)
            print(f"Getting data for page {page}")
            dict_params["pagination"]["currentPage"] = page
            sqs = json.dumps(dict_params)
            zillow_response = self.session.get(self.url,
                                               params={"searchQueryState": sqs,
                                                       "wants": '{"cat1":["listResults"]}'},
                                               headers={
                                                   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                                                             "image/avif,image/webp,image/apng,*/*;q=0.8,"
                                                             "application/signed-exchange;v=b3;q=0.7",
                                                   "accept-language": "en-US,en;q=0.9",
                                                   "authority": "www.zillow.com",
                                                   "cache-control": "no-cache",
                                                   "dnt": "1",
                                                   "pragma": "no-cache",
                                                   "referer": "https://www.zillow.com/search/GetSearchPageState.htm"
                                                              "?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22"
                                                              "%3A36.083312%2C%22east%22%3A-78.388787%2C%22south%22%3A35.869345%2C%22west%22%3A-78.719592%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForRent%22%3A%7B%22value%22%3Atrue%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A8%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A55006%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A1%7D%7D&wants={%22cat1%22:[%22listResults%22]}",
                                                   "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
                                                   "sec-ch-ua-mobile": "?0",
                                                   "sec-ch-ua-platform": "\"Windows\"",
                                                   "sec-fetch-dest": "document",
                                                   "sec-fetch-mode": "navigate",
                                                   "sec-fetch-site": "same-origin",
                                                   "upgrade-insecure-requests": "1",
                                                   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
                                               },
                                               cookies={COOKIES GO HERE!!})
            try:
                data = zillow_response.json()
            except requests.exceptions.JSONDecodeError:
                print(zillow_response.url)
                break
            else:
                results = data["cat1"]["searchResults"]["listResults"]
                final_results += results
                self.json_data = final_results
        return final_results

    def process_data(self, results: list[dict]) -> None:
        """takes a subset of JSON data as an argument as mutates the prices, addresses, and urls lists."""
        i = 0
        for result in results:
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


zillow_scraper = ZillowDataGetter()
zillow_scraper.get_zillow_data(5)
zillow_scraper.process_data(zillow_scraper.json_data)
big_ol_address_price_url_tuple_list = zip(zillow_scraper.addresses, zillow_scraper.prices, zillow_scraper.urls)
list_of_addr_price_url_tuples = [tuple for tuple in big_ol_address_price_url_tuple_list]

form_filler = FormFiller()
for tuple in list_of_addr_price_url_tuples:
    form_filler.find_inputs()
    form_filler.wait_for_forms_to_be_interactable()
    time.sleep(1)
    address, price, link = tuple
    form_filler.fill_input(form_filler.address_input, address)
    form_filler.fill_input(form_filler.price_input, price)
    form_filler.fill_input(form_filler.link_input, link)
    form_filler.submit()
    time.sleep(1)
    form_filler.get_next_form()
    time.sleep(1)