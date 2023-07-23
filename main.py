import bs4
import requests
from requests_html import HTMLSession

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import uncurl


def extract_prices(list_of_strings: bs4.ResultSet|list[bs4.Tag]) -> list[str]:
    examples = list_of_strings
    result = []
    for _ in examples:
        _ = _.text
        prices = _.count('$')
        dollars_and_more = _.split("$")[1:prices + 1]
        for _ in dollars_and_more:
            dollars = _.split("+")[0]
            result.append(dollars)
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

URL = "https://www.zillow.com/raleigh-nc/rentals/"

session = HTMLSession()
zillow_response = session\
    .get("https://www.zillow.com/raleigh-nc/rentals/", headers={
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
    }, cookies={
        "AWSALB": "Yn5H4/1ZSj5ZUD4AvxcZu4YwS6L4B6w9JrnA0ZTLrBT+0c67bVdfbMCHIjAhvY/k/lBrFf1y7r89xvPL3o5yJRyyOqsu1H7Y8ooKudG/ykD3xvfdZVh7uKZ04IjJ",
        "AWSALBCORS": "Yn5H4/1ZSj5ZUD4AvxcZu4YwS6L4B6w9JrnA0ZTLrBT+0c67bVdfbMCHIjAhvY/k/lBrFf1y7r89xvPL3o5yJRyyOqsu1H7Y8ooKudG/ykD3xvfdZVh7uKZ04IjJ",
        "JSESSIONID": "A58A0BFAB2292CE2DDEEC524944293B7",
        "_pxvid": "749d82bf-2814-11ee-a5ad-182dd0262840",
        "pxcts": "749d91aa-2814-11ee-a5ad-414746486b52",
        "search": "6|1692573393251%7Crect%3D33.605858864133445%252C-86.5147698271654%252C33.24769256121517%252C-87.05447319630602%26rid%3D73386%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0973386%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09",
        "zg_anonymous_id": "%22498a8667-b89b-4acb-9346-032c978ae200%22",
        "zgsession": "1|28a5e2e7-4ad0-400a-979f-a6aa28cab08c",
        "zguid": "24|%242fd81c75-a7eb-4517-ac9b-06cf624b83b0",
        "zjs_anonymous_id": "%222fd81c75-a7eb-4517-ac9b-06cf624b83b0%22",
        "zjs_user_id": "null"
    })
# print("Before: \n", zillow_response.json())
zillow_response.html.render(scrolldown=1, sleep=5)
zillow_zoup = BeautifulSoup(zillow_response.text, "html.parser")
links = zillow_zoup.find_all(attrs={"data-test": "property-card-link"})
span_tags = zillow_zoup.select("span")  # $ {price} + {type}
addresses = zillow_zoup.select("address")
examples = []
results = [_ for _ in span_tags if "$" in _.text]

prices = extract_prices(results)
print(f"{len(addresses)=}, {len(prices)=}, {len(links)=}")
for i, a in enumerate(addresses):
    print(prices[i])
    print(a.text)
    print(links[i].attrs["href"])