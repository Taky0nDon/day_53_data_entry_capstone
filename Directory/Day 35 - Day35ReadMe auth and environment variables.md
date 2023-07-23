D A Y T H I R T Y F I V E

# Lesson Goals

* api authentications
* * yse twillio to send SMS
* environment variables and how they can safely store API keys
* build a rain alert app

# <a name="api_authentication"></a> API Authentication
*API endpoint* The url to hit to get data

*parameters* different inputs to pass to API to get different data

Today we will use [openweathermap](https://www.openweathermap.org/)

An API key is something API providers use to prevent abuse of their services. They
allow the provider to track how much you are using the API, authorize access,
and deny once limit is exceeded.

[some text](#markdown-header-API-Authentication)

# lesson 2
## Using API keys on OWM

# Lesson 3
Exploring the data returned from OWM to determine if its going to rain today
run script at 7
check weather for next 12 hours
send text if its going to rain
if weather code < 600, then print("Bring an umbrella"

# Lesson 4
How to send a SMS with python using twilio

# Lesson 5
2## Using **environment variables** and hiding sensitive info
* create an environment variable
* show environment variables in the terminal: `Get-ChildItem env:`
* or set in cmd.exe
* environment variables allow you to change variables without having to edit code
* increase security so sensitive info is not in the code:
  * passwords
  * API keys
  * API auth stuff
* The only way I could get environment variables to work was by setting them through
* the edit run configuration dialog in PyCharm.
* ### PyCharm runconfigurations are stored in workspace.xml in the .idea folder.
* ### todo: look into setting environment variables on windows more
* ### todo: checkout apilist.fun
* 