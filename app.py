import pandas as pd

"""
print("Hello World")

data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame)

serie = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(serie)

fechas = pd.date_range(start="2021-05-01", end="2021-05-12")
print(fechas)

my_series = pd.Series([2, 4, 6, 8, 10])
my_series = my_series.apply(lambda i : i/2)
print(my_series)

data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
df = pd.DataFrame(data, columns=["Brand","Model","Color"])
print(df)

data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    },
    {
        "brand": "Tesla",
        "model": "Model S",
        "color": "Red"
    }
]
df2 = pd.DataFrame(data)
print(df2)
"""

data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")

"""
print(data_frame.iloc[133,6])

print(data_frame.head(3))

print(data_frame.tail(3))

print(data_frame[["Name","Type 1"]].head(10))

print(data_frame.loc[data_frame["Attack"]>80])

legenda = len(data_frame.loc[data_frame["Legendary"]== True])

print(legenda)
"""
baby_names = pd.read_csv(".learn/assets/us_baby_names_right.csv")

print(baby_names.head(5))
baby_names = baby_names.drop("Unnamed: 0", axis=1)
print(baby_names.head(5))

print(baby_names.value_counts("Gender"))

baby_names = baby_names.groupby("Name").sum()

tamaño = len(baby_names)

print(tamaño)
