import pandas
data = pandas.read_csv("4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
# print(fur_color)
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])

# creating a data frame

squirrels_short_data = {
    "squirrels_color": ["Cinnamon", "Black", "Gray"],
    "population": [cinnamon, black, gray]
}
data = pandas.DataFrame(squirrels_short_data)
data.to_csv("new_squirrels_data")




