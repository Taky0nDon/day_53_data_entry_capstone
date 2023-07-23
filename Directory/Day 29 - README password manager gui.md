D A Y T W E N T Y N I N E
# BUILDING A PASSWORD MANAGER

![logo.png](C:\Users\Mourn\100_days_of_code\day_29_password_manager\logo.png)


CHECK OUT THE CODING HORROR BLOG
MyPass
Website_label: w_entry (width = 35)
Username_label: u_entry (width = 35)
Password_label: p_entry (width = 21)
add_button (width=36)

when add is clicked, you get a pop up to confirm
pop up telling you to complete all fields if any field is empty
clicking generate password automagically saves the pw to the clipboard

window title = "Password Manager"
* the Tk() class creates a window
200x200 canvas with 20px x and y padding
image centered on canvas

# MORE ABOUT THE GRID
* time to learn about span!
* columnspan = {number of columns the widget takes up}

###### app layout: 3 col, 5 row

# set default cursor position
* use the focus() method
# set default entry text
* use the insert() method
  * insert(index string)
  * index: where to insert {string}
  * index = END - the final character of the entry

# save info to file

<{website}> | <{username}> | <{password}>

# clear entry text
* use the delete({start}, {end}) method

# Dialog Boxes and Pop-Ups
* Standard Dialogs
  * messagebox module
    * messagebox.showinfo(title, message)
* I told the user which field(s) they forgot to enter

# pyperclip