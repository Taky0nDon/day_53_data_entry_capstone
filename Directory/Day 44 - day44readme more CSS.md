[[Day 43 - readme CSS]]
# D A Y F O R T Y F O U R

## Color Properties

### `background-color`

### `color`
### Named Colors
`<named-color>`

[color hunt](https://colorhunt.co)

rgb colors are a fraction of 255

## Font Properties

color
font-weight: normal or bold; lighter+-100/bolder+-100 (relative to parent); 100 - 900 (light to bold) number
font-size
font-family: font-name, generic-font-type
`html {
  font-family: Helvetica, sans-serif;
}
h1 {
  font-family: "Times New Roman", serif
  }

[Browse Fonts](https://fonts.google.com)

copy the link and add it to the HTML in the head element under the style, and then add the CSS rule to the desired elements

1 px ~= 1/96 inch
1 pt ~= 1/72 inch
most font sizes in text editors are in points
1em = 100% of parent (element enclosing element in question)
2em = 200% of parent size
1rem = 100% of root (master element, usually html)
rem is more consistent since it only relative to the root element

### text alignment
`text-align: center, left, right, start, end`
start and end are relative to the language

## CSS Inspection

## Box Model

Margin
```border: {thickness}{style}{color}
border-top:
border-width: {top}{right}{bottom}{left} | {top and bottom}{left and right}
 ```
Padding
element Width
element Height

## Div time!

content division element is used to group elements together to apply style rules to
