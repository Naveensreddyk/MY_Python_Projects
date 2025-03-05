import pandas

# Load the data
#we are reading the CSV file Using pandas and assigning it to a new variable.
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250222.csv")

# Extracting the 'Primary Fur Color' column from the squirrel data and assigning to a new variable.
all_colors = squirrel_data["Primary Fur Color"]

# Filter the data based on different fur colors and finding its count using the length method.
gray_color_count = len(squirrel_data[all_colors == "Gray"])
cinnamon_color_count = len(squirrel_data[all_colors == "Cinnamon"])
black_color_count = len(squirrel_data[all_colors == "Black"])

#Created a new dictionary key and value
squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color_count, cinnamon_color_count, black_color_count]
}
#Created a new table or the new data frame by passing the dictionary.
new_color_data = pandas.DataFrame(squirrel_dict)
print(new_color_data) #printing the new table.



