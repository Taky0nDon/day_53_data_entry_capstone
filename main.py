import bs4
import requests
from requests_html import HTMLSession
import json
from typing import IO

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import uncurl


def extract_prices(text: str) -> str:
    return text.split("$")[1].split("+")[0]

def cookies_to_list_of_dict(cookie_file: str) -> list[dict]:
    result = []
    with open(cookie_file) as file:
        cookies = file.readlines()
    for cookie in cookies:
        parts = cookie.split("=")
        name = parts[0]
        value = parts[1]
        new_cookie = {"name": name, "value":value}
        result.append(new_cookie)
    return result


ZILLOW_HEADERS = {
      # :Authority:
      # www.zillow.com
      # :Method:
      # GET
      # :Path:
      # /raleigh-nc/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22undefined%22%2C%22mapBounds%22%3A%7B%22north%22%3A36.13404906298567%2C%22east%22%3A-78.08578563085936%2C%22south%22%3A35.43779278800827%2C%22west%22%3A-79.16519236914061%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54047%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D
      # :Scheme:
      # https
      "Accept":
      "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "Accept-Encoding":
      "gzip, deflate, br",
      "Accept-Language":
      "en-US,en;q=0.9",
      "Cache-Control":
      "no-cache",
      "Cookie":
      "zguid=24|%242fd81c75-a7eb-4517-ac9b-06cf624b83b0; zgsession=1|28a5e2e7-4ad0-400a-979f-a6aa28cab08c; zjs_anonymous_id=%222fd81c75-a7eb-4517-ac9b-06cf624b83b0%22; zjs_user_id=null; zg_anonymous_id=%22498a8667-b89b-4acb-9346-032c978ae200%22; JSESSIONID=A1DC6120E27CA461626B5B57DD1EABA7; pxcts=749d91aa-2814-11ee-a5ad-414746486b52; _pxvid=749d82bf-2814-11ee-a5ad-182dd0262840; _px3=d3ec54f73f6032c0ee885826ac42ea5ac6400def9f75ce1895be414ebed56605:42ZN8Y3H8r8PXV54PZAMc7GcUZge8BrTbGrRj5KrJHTfyP8eIvhMq7kQBiSydxLRKXOegJBiW6zpGvh1nQeGCQ==:1000:R49mA5M+rrlg0EdoSWZC955DZisl/rI4lnsF3MHD7wFTeHjiPQGsAabX7my6r7Xhf9zrqS1xeEhG1pLo68vhS6xMVtfz3h1I8BNpufP5U7ekUjwGJhN8m/6jM+d+diOl3c3hlp5U9xrmaXZI+JC4rd0D0VY8agQfnodjdYRmrYhZyq4G7mHkpeGbJdBLw7M0Lz2hB6AUKGqFGaEDktLRjg==; search=6|1692570938581%7Cregion%3Draleigh-nc%26rb%3Dundefined%26rect%3D36.009543%252C-78.431929%252C35.563197%252C-78.819049%26disp%3Dmap%26mdm%3Dauto%26sort%3Dpriorityscore%26listPriceActive%3D1%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%09%0954047%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; AWSALB=rXiXr9c6F+MxNDdjrXO9UAGoUbEDVvG+djb/Fp9Feb3FqKuyebcdOMpwWHishp08jua3tM5LIZ5MOXPqUP2FPgRfxdzHzVdugnmnX4JfggMVaLlFYBmXdwuBEJEw; AWSALBCORS=rXiXr9c6F+MxNDdjrXO9UAGoUbEDVvG+djb/Fp9Feb3FqKuyebcdOMpwWHishp08jua3tM5LIZ5MOXPqUP2FPgRfxdzHzVdugnmnX4JfggMVaLlFYBmXdwuBEJEw",
      "Dnt":
      "1",
      "Pragma":
      "no-cache",
      "Sec-Ch-Ua":
      '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
      "Sec-Ch-Ua-Mobile":
      "?0",
      "Sec-Ch-Ua-Platform":
      "Windows",
      "Sec-Fetch-Dest":
      "document",
      "Sec-Fetch-Mode":
      "navigate",
      "Sec-Fetch-Site":
      "same-origin",
      "Sec-Fetch-User":
      "?1",
"Upgrade-Insecure-Requests":
      "1",
      "User-Agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
page_number = 1
URL = "https://www.zillow.com/raleigh-nc/rentals/"


session = HTMLSession()
# my_cookies = cookies_to_list_of_dict("cookies.txt")
# for cookie in my_cookies:
#     n = cookie["name"]
#     v = cookie["value"]
#     session.cookies.set_cookie(n, v)
raw_params = '{"mapBounds":{"west":-78.719592,"east":-78.388793,"south":35.869345,"north":36.09583},' \
             '"isMapVisible":false,' \
             '"filterState":{"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},' \
             '"cmsn":{"value":false},"auc":{"value":false},"fr":{"value":true},"ah":{"value":true}},' \
             '"isListVisible":true,' \
             '"pagination":{"currentPage":2}}'
dict_params  = json.loads(raw_params)
for _ in range(1,2):
    page_number = _
    # print([k for k in dict_params.keys()])
    dict_params["pagination"]["currentPage"] = _
    sqs = json.dumps(dict_params)

    parameters = {"searchQueryState": sqs,
                  "wants": '{"cat1":["listResults"]}'
    }

    dumped_params = json.dumps(parameters)

    print(f"Page {_}: ")
    url = "https://www.zillow.com/search/GetSearchPageState.htm"
    zillow_response = session\
        .get(url, headers={
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "authority": "www.zillow.com",
            "cache-control": "no-cache",
            "dnt": "1",
            "pragma": "no-cache",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        },
             params=parameters,
             cookies={
                 "_px3": "3610e2a84c70122debde195f381996766eda325c8e2b46c55ac92de65904e316:uUQvCkrWDIDIlrtrQ4fhT/rCWxLTrcFbT2k4n12De7pBHUITX18fAtH8MhpYhscZSc+9y7BTQuOXunkoqooiIQ==:1000:wvG51Oxp7m7VnxtK8Kg9RaFN+xcQT1taFdkaz/pkAvGC0HkEYv5rzx5RSIe5YsH8ms4o+lCYYXHiSQkWeIcQl4IQrsF1EYN71brbzSqqa1Y3MwVlOJ3O0Dh5acqqJraPCIKD37qb8uqlmAl4lw7ThKXkpuXgBEkk4UOF8tT09XGVCLAaFDecJvdM2Bs15PL00xgP+zez5n67hlTE1iuBbg==",
                 "_pxff_bsco": "1",
                 "_pxff_cc": "U2FtZVNpdGU9TGF4Ow==",
                 "_pxff_ccc": "1",
                 "_pxff_cfp": "1",
                 "_pxff_fp": "1",
                 "_pxff_rf": "1",
                 "_pxvid": "4f8815a7-2a86-11ee-a047-faa9b5fc5718",
                 "pxcts": "4f882716-2a86-11ee-a047-49526b4f6276"
             }
             )
    cookies = session.cookies
    for cookie in cookies:
        with open("zillowcookies.txt", "a") as file:
            file.write(str(cookie) + "\"n")
    print(zillow_response.text)
    data = zillow_response.json()
    results = data["cat1"]["searchResults"]["listResults"]
    for result in results:
        prices = result["units"]
        unit_price = prices[0]["price"]
        unit_beds = prices[0]["beds"]
        unit_address = result['address']
        info_string = f"The price of this {unit_beds} br unit is {unit_price}. It is located at {unit_address}."
        url = result["detailUrl"]
            print(info_string)
            print(f"Check it out: https://www.zillow.com/{url}")

    # zillow_response.html.render(scrolldown=3, sleep=5)
    # zillow_zoup = BeautifulSoup(zillow_response.text, "html.parser")
    # links = zillow_zoup.find_all(attrs={"data-test": "property-card-link"})
    # span_tags = zillow_zoup.select("span")  # $ {price} + {type}
    # addresses = zillow_zoup.select("address")
    # examples = []
    # strings_containing_price = [_.text for _ in span_tags if "$" in _.text]
    # print(f"{len(addresses)=}, {len(strings_containing_price)=}, {len(links)=}")
    # for i, a in enumerate(addresses):
    #     print(f"Price: ${extract_prices(strings_containing_price[i])}")
    #     print(f"Address: {a.text}")
    #     print(f"Link: https://www.zillow.com{links[i].attrs['href']}")