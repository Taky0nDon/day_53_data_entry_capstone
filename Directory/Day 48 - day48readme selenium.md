# D A Y F O R T Y E I G H T
[[Day 50 - day50readme more selenium]]
[[Day 51 - DAY51README even more selenium]]

## Selenium

* Allows automated tested of web sites and apps.
* Automate filling in forms

## How to begin using Selenium
1. Install Chrome
2. Download Chrome Driver
   * Make sure you get the file path
3. Install and setup Selenium

   *`from selenium import webdriver`

## What is the chrome driver?
   * the chrome driver bridges the selenium code and the browser

## driver.get({page})
   * opens a browser window
   driver.get vs driver.close():
     * close() just closes the active tab
   * Keeping the browser window open:
```python
chrome_driver_options = selenium.webdriver.chrome.options.Options()
chrome_driver_options.add_experimental_option("detach", True)
```
   *then pass `chrome_driver_options` to the driver class
## How to find and select elements with Selenium:
use the webdriver method find_element, and the
by argument is a By object, which comes from `selenium.webdriver.common.by`
```python
driver.get("https://www.amazon.com/Ghost-World-Daniel-Clowes/dp/0224060880/ref=pd_vtp_h_pd_vtp_h_sccl_2/130-9885068-6733334?pd_rd_w=CSAwu&content-id=amzn1.sym.e16c7d1a-0497-4008-b7be-636e59b1dfaf&pf_rd_p=e16c7d1a-0497-4008-b7be-636e59b1dfaf&pf_rd_r=WAE7VSZWSS63BRE3KSBA&pd_rd_wg=iHuML&pd_rd_r=f7dc1dde-4412-4921-947a-f6d1c5647643&pd_rd_i=0224060880&psc=1")
price_element = driver.find_element(By.ID, value="price")
find_by_css_selector = driver.find_element(By.CSS_SELECTOR, value ="#cm-cr-local-reviews-title" )
some_review = driver.find_element(By.XPATH, value='//*[@id="customer_review-R2ASHY83PDM2N2"]/div[4]/span/div/div[1]/span')

print(price_element.size)
print(price_element.screenshot_as_png)
print(price_element.tag_name)
print(price_element.get_attribute(name="class"))
print(price_element.get_property(name="attributes"))
print(find_by_css_selector.get_attribute(name="class"))
print(some_review.text)
```
## XPath
* A way of locating a particular HTML element

## Interacting with the page
* typing into an input field
* clicking on a button
### How to click

* get hold of the element and call `.click()` on it.
* input text with `sendkeys()`
* use the `Keys` class to send special keys like enter. found
in selenium.webdriver.common.keys

## Final Project
* Cookie clicker!
* maximize cookies / second