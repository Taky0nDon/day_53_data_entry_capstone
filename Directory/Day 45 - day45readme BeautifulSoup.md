#  D A Y F O R T Y F I V E

## BeautifulSoup
[[cheat_sheet BeutifulSoup]]

BS is an HTML parser
Scrape empire's 100 greatest movies of all time and pull out relevant pieces:

* title
* ranking
* watched

## Using BS4

`from bs4 import BeautifulSoup`

`soup = BeautifulSoup(content, "html.parser")`
#### can also use xml parser

### markup=content html.parser = parser
### soup.a gives the first anchor tag
### soup.prettify() will format the HTML
### soup.li, soup.p gives first li, p respectively

### What if you want all the occurrences of a given tag?

```
title = soup.title
print(title, "\n", title.name, "\n", title.string)
```

## soup.find_all() -> list
name: tag name
id: tag id name
class_: tag class name
searches for all occurrences of a tag

### tag.getText() 
* returns the string enclosed in a tag
* getText() vs tag.string ?

### tag.get(attribute: str) -> str
* returns the string assigned to any html attribute

### What if you want to find a specific anchor tag?

* Use soup.select() and soup.select_one() to find a particular
tag with CSS selector syntax. So to find an anchor tag nested
within a p tag, you would set the selector parameter to "s a"
* It also works with id and class selection syntax
* select_one() returns the first match, select() returns
a list of all matches

## The Ethics of Scraping

### Genius vs Google - Genius loses
### hiQ vs Linkedin - LinkedIn loses

### You can scrape a websites data as long as you:
* scrape public, not copywritten data
* cant commercialise copyrighted content
* cant scrape data behind authentication
  * you agree to not use the data commercially when you create an account and accept the TOS

### Preventing webscraping:
* captcha
* reCAPTCHA - newer version
  * looks at mouse movement on the way to check box, as well as other
  collected data

### Webscraping Ethics
* consider the golden rule
* Use public API over webscraping when possible
* Respect the web owner:
  * check url-root/robots.txt

## Project: 100 Movies to Watch

* Scrape a list of
[top 100 movies](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/) to pick one to watch
* 