# D A Y T W E N T Y F I V E

## how to work with data files
~~~
with open("weather_data.csv", "r") as weather_data:
    weather_data_list = weather_data.readlines()
print(weather_data_list)


import csv

with open("weather_data.csv") as data_file:
    data = list(csv.reader(data_file))
temps = []
for row in data:
    if row == data[0]:
        continue
    temps.append(int(row[1]))
 print(temps)
import pandas
data = pandas.read_csv("weather_data.csv") #DataFrame, composed of series. every column is a series
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
result = sum(temp_list)
avg_temp = result / len(temp_list)
print(avg_temp)
print(data["temp"].mean())
print(data["temp"].std())
print(data.condition.mode())
#get data in the rows
print(data[data.day == "Monday"]) #return Monday's row
# CHALLENGE get row with max temp
max_temp_row = data[data.temp == data.temp.max()]
monday = data[data.day == "Monday"] #returns the "Monday" row as a Series
#convert monday temp to F
# F = (1/5)((9)C - 32)
def get_F(C):
    return ((9/5)*C + 32)
print(get_F(monday.temp))
print(type(monday.temp))
~~~
## create a dataframe from scratch
~~~
import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
~~~
passing a dict into pandas.DataFrame() returns a new data frame
calling the to_csv() method on a dataframe writes a new CSV file where the
argument is the path