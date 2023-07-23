SOLUTION

GOAL ONE:

1. add city IATA code to google sheet
1.1 make requests using the kiwi partners tequila api
    endpoint = 
1.2 pass each city name in sheet_data one-by-one to FlightSearch class to ge the corresponding IATA code for that city
1.3 use the code you get back to update the sheet
    1.3.1 for some reason you have to use json instead of data in the PUT request
        the `json` parameter adds the "content-type": "application/json" to the header and converts the dict to JSON
        `data` takes a dict or a string. passing a dict is useful if the data to send is form-encoded

# pip install gspread

```
commandline
import gspread

sa = gspread.service_account(filename="path/to/service/file")
```