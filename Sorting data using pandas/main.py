# import csv

# with open("weather_data.csv") as weather_data:
#     weather = csv.reader(weather_data)
#     temperatures = []
#     for row in weather:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#pandas is a library used for data manipulation and analysis and providing efficient data structures like DataFrames and Series.
# import pandas #we imported pandas library here.
# data = pandas.read_csv("weather_data.csv") #reading the weather.csv file using pandas
# print(data["temp"]) #we are printing the temp column in the weather_data.csv
import pandas
data = pandas.read_csv("weather_data.csv") #pandas reading the weather_data csv file and stored the info in a variable called data.
temp_list = data["temp"].to_list() #We are converting the data in the temp to a list.
#Here data["temp"] is the series. So, the syntax is "series.mean()"
average = data["temp"].mean() #mean is the method of panda to calculate the average in the series.
print(average)
max_value = data["temp"].max() #prints out the maximum value in the series.
print(max_value) #prints out the maximum value.
print(data.day) #easiest way to print out the column day from the data variable.
print(data.condition) #print out the condition column.
#IF we want to print out the row....
print(data[data.day == "Monday"]) #First we are getting hold of the complete data and then getting into the column and then calling the row.
#We are actually getting hold of the maximum temperature and printing the entire row which has the maximum temperature.
print(data[data.temp == max_value])
#We are actually getting the monday's temperature and converting it to fahrenheit.
Monday = data[data.day == "Monday"] #I created a variable Monday and getting hold of the data.
Fahrenheit = (Monday.temp * 9/5) + 32  #coverting the temperature.
print(f"Current Temperature is {Fahrenheit}F") #printing it out.

#Creating a DATAFRAME/TABLE from scratch below is the example.
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [89,90,50]
}
#here we are creating a new dataframe by calling the DataFrame class from the Pandas Library and entering out dictionary name.
fresh_table = pandas.DataFrame(data_dict)
print(fresh_table)

