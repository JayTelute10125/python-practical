import pandas as pd

# Sample data structure based on your image
data = {
    'carat': [0.23, 0.21, 0.23, 0.29, 0.31],
    'cut': ['Ideal', 'Premium', 'Good', 'Premium', 'Good'],
    'price': [326, 326, 327, 334, 335],
    'x': [3.95, 3.89, 4.05, 4.20, 4.34],
    'y': [3.98, 3.84, 4.07, 4.23, 4.35],
    'z': [2.43, 2.31, 2.31, 2.63, 2.75]
}
df_diamonds = pd.DataFrame(data)

# i) Mean price for each cut
print("Mean Price by Cut:\n", df_diamonds.groupby('cut')['price'].mean())

# ii) Count, Min, and Max price for each cut
stats = df_diamonds.groupby('cut')['price'].agg(['count', 'min', 'max'])
print("\nPrice Stats by Cut:\n", stats)

# Average value of x, y, and z separately
print("\nAverage x:", df_diamonds['x'].mean())
print("Average y:", df_diamonds['y'].mean())
print("Average z:", df_diamonds['z'].mean())