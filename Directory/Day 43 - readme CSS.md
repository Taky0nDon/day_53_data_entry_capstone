D A Y F O R T Y T H R E E
[[Day 44 - day44readme more CSS]]
# CSS
## Cascading Style Sheets

Styling starts from most general and progressively gets more specific.
A style sheet is a type of language
SASS = syntactically awesome style sheet
Less = leaner CSS

## Origins of CSS

Marc Andreesson email
Want to control what your documents look like? Sorry, you're screwed if you want to use HTML.
w3c (w3 Consortium) released HTML 3.2 in 199*, introducing
* The font tag
* color, face, size attributes for font
* center element
* All of which are now deprecated, because HTML is meant for content, not styling.

introducing CSS in dec 96, now you can attach style to HTML docs. Demonstrates `separation of concerns.`

[What can CSS achieves?](https://appbrewery.github.io/just-add-css)

## ways of adding CSS
### Inline
Goes into the same line as a certain HTML element via a `style` attribute.
Good for adding styling to a single element, but why would you want to do that? It's cumbersome.
```
<html style="background: blue">
</html>
```

### Internal CSS
Use the style element. Useful for applying style to a single document.
```
<html>
  <head>
    <style>html{
      background: red;
      }
    </style>
  </head>
</html>
```
in the above, `html` is a selector and the CSS goes in curly braces
### External
styling lives in a separate css file
put reference to CSS file in a link element in the  head    
rel = relationship

```
<html>
  <head>
    <link
      rel="stylesheet"
      href="./styles.css"
    />
  </head>
</html>
```
### CSS code format:
selector{
property: value;
}

## CSS Selectors
Help us choose where to apply CSS
* Element selector:
  chooses a single tag and applies that style to all instances of that tag
### Class Selector

```
.class-name{
  property: value;
}
```


* what is a class?
* its something we can add as an attribute to any HTML element.
* Used for grouping elements to apply same CSS rules too

`<p class="red-paragraph">some text</p>`

### Id selector

```
#main{
  color: red;
}
```
selects all elements with a given id attribute

`<p id="main">some text</p>`


### id vs class?

* class can be applied to many elements
* id only applied to a single element per html file (ideally)

### attribute selector

```
p[draggable]{
  color: red;
}

element[attribute=value]{
  property: value;
}
```

selects elements with particular attributes or attribute values

### Universal Selector

```
*{
  property: value;
}
```
