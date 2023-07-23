D A Y T H I R T Y

# ERRORS & EXCEPTIONS
## try / catch
* TRY
  * comes before code that might cause an exception
* EXCEPT
  * what to do if the try block causes an exception
  * avoid "bare except"
  * you want to be able to account for specific errors
  * capture error message
    * except <error type> as error_message:
* ELSE
  * what to do if there was no exception
* FINALLY
  * run this code regardless of exception status
## Raise your own exceptions
* raise
  * allows you to raise your own exception
* when to raise errors?
  * when code is valid but result would still be incorrect
  * ie user input is outside bounds
# JSON
```
with open(path/to/json) as file:
	dictionary = json.load(file)
```
* the above will load the json data into a python dictionary
* json is kind of like a dictionary
* import json
* json.dump(file, outputfile, indent) # write
	* requires file object to work, just like load.	
  * takes what to dump and where to dump it as parameters (see password mgr for example)
  * indent=(# of spaces to indent)
  * loads and dumps methods take strings instea of file objects
  * `json.dumps(dict) dict -> str
	`data = json.dump(data_to_dump, where_to_dump, indent=4)`
* json.load() # read
  * converts contents to a dictionary
  * JSON in, dict out
* json.update() #update
	*object_to_update.update(thing_to_update_with)
	*json_object.update(key_value_pair)
	*key_value_pair is appended to json_object
~~~
{
  "amazon":{
      "username": "username01",
      "password": "badpassword"
   }
}