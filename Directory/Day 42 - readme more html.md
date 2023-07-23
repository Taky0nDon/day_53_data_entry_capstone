D A Y F O R T Y T W O

# HTML Boilerplate

## DOCTYPE

`<!DOCTYPE html>`

## ROOT

```
<html lang="en">

</html>
```

## HEAD - page meta data

```commandline
<head>
    <meta charset="UTF-8">
    <title>My Website</title>
    
</head>
```

## BODY - goes under body

```
<body>
    <h1>Hello World!</h1>

</body>
```

lets put it together:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My Website</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
</html>
```

## The list Element

### Ordered
```
<ol>
    <li>xx</li>
</ol>
```

### Unordered

```
<ul>
    <li>xxx</li>

</utl>
```

## Nesting and Indentation

```
<ul>
    <li>A sublist:
        <ul>
            <li>First item of sublist</li>
        </ul>
    </li>
    <!-- Closing tag goes after the nested list -->
    <li>Next top-level item</li>
</ul>
```

## Anchor elements

`<a href="theurl.com" draggable=true>This is a link</a>
<tag attribute=value anotherattribute=value>content</tag>

## Global attributes
apply to any HTML element. ie: draggable=bool

## Image Elements
<img src="https://picsum.photos/200" alt="alternative text description of image" title="H O V E R T E X T"/>

[Lorem picsum](https://picsum.photos)
picsum.photos/size