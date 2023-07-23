#  D A Y T W E N T Y F O U R

# reading and writing to file

# add a highscore to snake

~~~
python

	def some_func():
~~~

# add self.highscore = 0 to the ScoreBoard class
# replace game_over with reset(self)
	~~~
	if self.score > highscore:
		self.highscore = self.score 
	self.score = 0
	self.update_scoreboard()
		~~~

#### add self.clear to update_scoreboard()

~~~
self.write(f"Score: {self.score} High Score: {self.highscore})
~~~

#### remove game_on = False and replace with scoreboard.reset()
#### create reset() method for Snake class

~~~
def reset(self):
	for segment in segments:
		segment.goto(1000, 1000)
	self.segments.clear()  # clear list of segments 
	self.create_snake()
	self.head = self.segments[0]
~~~

### RE_INITIALIZING snake and sending old snake off screen

## MAKE HIGHSCORE PERSISTENT

# files!

! open(file, mode, etc)
~~~
file = open("hi_score.txt", mode="a") OR with open("hi_score.txt") as file:
	contents = file.read()
	print(contents)
#with keyword manages file directly and automatically closes it
#mode "a" = append
	file.write("\nNext text.")
#if you write a file that doesnt exist, python will create it

# # file = open("my_file.txt"
# with open("my_file.txt") as file:  # with open(file.path) as variable:
#     content = file.read()  # returns contents of file as a string
#     print(content)

# write to file
~~~
with open("my_file.txt", mode="a+") as file:  # mode="w" overwrites contents. "a" adds them
    file.write("\nNew text.")
with open("new_file.txt", "w") as file:
    file.write("You just made a new file.")
~~~

##file paths and directories

"/" = root
/path/to/file/file.txt - absolute filepath

working directory - folder youre currently in
relative file path: ./file.txt
"./" = look in current folder
"../" = look in parent folder