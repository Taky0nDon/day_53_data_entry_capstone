# day_27_tkinter
day 27 of 100 days of code
## creating windows and labels with tkinter

* class Tk()
* need a way of keeping the window on the screen
  * mainloop() method of Tk class, must be last line in program
*class Label()
  * pack() method necessary to make label centered
    * this is "the packer"
  * a geometry management system, handles component layout
*Font
  * (name, size, bold/italic/etc)
* Buttons
* Entry
  * get user input
  * return input with get() method
* Setting Component Options

### [more tk stuff](./more_tk_stuff.py)

## I FOUND A LEGIT REASON TO USE A LAMBDA FUNCTION!
not just looking cool.
When you want to call a function WITH ARGUMENTS, but only have it called after an event (like a mousclick)
you call a lambda function that calls the function you want to pass arguments to.:
~~~
button.config(command=lambda: foo(bar))
~~~

## advanced function arguments
* **kw
* default values, use = when declaring parameters:
~~~
  def foo(x="bar"):
    return x
print(foo())
~~~
outputs "bar" when no arguments given
* *args many arguemnts. UNLMITED POSITIONAL ARGUMENTS
~~~
  def add(n1, n2):
    return n1 + n2
~~~

becomes

~~~
def add(*args):
  for n in args:
    print(n)
~~~
given arguments form a tuple

### now for unlimited keyword args?
  * **kwargs
~~~
def calculate(n, **kwargs):
  # kwargs is a dictionary keyword:valuee
  for key, value in kwargs.items():
    print(f"{key} : {value}")
  n +=1 kwargs["add"]
  n *= kwargs["multiply"]
  
class Car:
  def __init__(self, **kwargs):
    self.make = kwargs["make"]
    self.model = kwargs.get("model")  # if "model" isnt in dict, returns None-
my_car = Car(make="Toyota", model="Camry")
calculate(2, add=2, muliply=5)
~~~

# layout managers
1. pack()
   * starts from the top and packs every widget below the previous one
   * change with parameters
2. place()
  * lets you place widgets with x and y coordinates. 0, 0 = top left
3. grid()
    * can place with a column and row #. grid is relative to other components
# padding
padx, pady : add space around widgets

# [project: convert miles to km](./mi_to_km.py)