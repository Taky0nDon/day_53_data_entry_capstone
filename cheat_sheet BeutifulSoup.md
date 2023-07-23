Detailed docs: [the Beautiful Soup 4 Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
#beautifulsoup


Assume `t` is an object of `Tag`.

## Core concepts (classes)

- `Tag`, a Tag object corresponds to an XML or HTML tag.
- `BeautifulSoup`, the BeautifulSoup object represents the parsed document as a whole. You can treat it like a special Tag. It needs a parser to parse the document, a built-in parser is `"html.parser"`, e.g. `soup = BeautifulSoup("<html>a web page</html>", 'html.parser')`
- `NavigableString`, a string corresponds to a bit of text (as you see it in the browser) within a tag. A NavigableString is just like a Python Unicode string, except that it also supports some of the features for navigating the tree and searching the tree.

## The `Tag` class

Object attributes:

- `t.name`, the text inside the angle brackets, for example, `<a>`
- `t.attrs`, accesses all attributes of a tag as a dict
- `t["foo"]`, gets the HTML/XML attribute of "foo", set it by `t["foo"] = "bar"` Beautiful Soup presents the value(s) of a multi-valued attribute as a list, e.g. `t['class']`
- `t.string` gets the text within a tag
- `t.get_text()` gets the human-readable text as a string inside a document/tag

## Navigating the tree

- get the first tag by its name, e.g. `t.head`, `t.title`
- get all **direct** children as a list by `t.contents`, or using the `.children` generator, e.g. `for tag in t.children: pass`
- `t.parents` to iterate over all of an element's parents
- `t.previous_sibling, t.next_sibling` to go sideways, or `t.previous_siblings, t.next_siblings` to iterate over siblings.

## Searching the tree

Filter types:

- A string
- A regex
- A list
- A function

Search methods:

- `t.find_all()` looks through a tag’s descendants and retrieves all descendants that match your filters
	- `attrs = {"name": "value"}`
- `t.select()` matches elements by using CSS selectors
- `t.find()` likes `find_all()` but it only finds one result
- `t.find_parents()` and `t.find_parent()`
- `t.find_parents()` and `t.find_parent()`
- `t.find_next_siblings()` and `t.find_next_sibling()`
- `t.find_previous_siblings()` and `t.find_previous_sibling()`

## Debugging

- `print(t.prettify())` pretty-prints the tag
- `print(t)` prints the html without beautification
- `type(t)` shows the type of an object
[source](https://whatacold.io/blog/2021-12-05-beautifulsoup4-cheatsheet/)