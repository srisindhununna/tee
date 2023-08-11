import pandas as pd
df = pd.read_csv("task1.csv")
grouped = df[df['My_Gender'] == 'Male'].groupby('My_City')['My_Population'].sum()
city_with_highest_male_population = grouped.idxmax()
print(f"The city with the highest male population is: {city_with_highest_male_population}")