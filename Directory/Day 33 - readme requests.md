D A Y T H I R T Y T H R E E

# python anywhere

[python anywhere](https://www.pythonanywhere.com)

## Schedule a task:
### Dashboard => Tasks => Schedule Task
* ### Enter command to run at given time
    ex: `python3 /path/to/main.py`

# Today's Goal

* install jsonviewerawesome
* using APIs or Application Programming Interfaces
* Track current position of ISS
* Email us when ISS is above us

## What is an API anywway?
* A way for you to access data
* ### A set of commands, functions, protocols and objects programmers can use
  to create software or interact with an external system
* Pull live data from websites
* [Your program] | [External System]
                 ^ API
* An API is a set of rules for interacting with the external system

## API endpoints and making API calls
* ### API endpoint:
  * it's like a location
  * where the desired data is stored
  * it can be a URL
  * ex:
  * http://api.open-notify.org/iss-now.json <= this is the endpoint
    * for the ISS location

* ### API Calls:
[[HTML encoding]]
[[Day 30 - README Try, Catch, Json]]
  * GET requests
    * trying to get a piece of data
    * use the `requests` library
      * `response = requests.get(url=string)`
      * `print(response)` returns `<Response [200]>`
      * 200 is a **response code**

| Response Code | Meaning       |
|---------------| ------------------------------ |
| 404           | resource not found |
| 1XX           | Hold on, something's happening |
|  2XX          | Here, request successful |
 | 3XX           | Permission Denied |
 | 4XX           | Screwed up    |
    * more @ httpstatuses.com
    * get more details of `response`
      * `response.status_code` returns an int
    * requests can generate an exception based on the response code
      * `response.raise_for_status()`
    * tap into json response :
      * `response.json()` returns a dictionary
    * iss timestamp is a unix time stamp:
      * seconds since 1/1/1970
    * # project idea: unix time stamp converter
    * latlong.net to find coordinates on globe
``
### API parameters

   * Allow you to give your requests inputs that change what is received
   * Get more specific data
   * Sunrise sunset API
     * [sunrise-sunset](https://api.sunrise-sunset.org/json)
   * Enter parameters in a URL string
     * **URL/json?param1=value1&param2=value2&paramn=valuen**
     * ENDPOINT ? PARAM = VALUE & MORE_PARAM = MORE_VALUE
```
https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400

https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today

https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=2023-05-11

https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0
```

### Kanye Quotes
  * use request module to get `get_quote()` to work, so each time
  * button is pressed, canvas text is changed to quote

### ISS Challenge:
If the ISS is near my current location
AND
It is currently dark
(if now.hour < sunrise or now.hour > sunset)
THEN
send me an email
run every 60 seconds