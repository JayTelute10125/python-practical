import pandas as pd

# Create initial table for 5 states
data = {
    'State': ['Maharashtra', 'Texas', 'California', 'Bavaria', 'Goa'],
    'Area': [307713, 695662, 423970, 70550, 3702],
    'Population': [112374333, 29145505, 39538223, 13076721, 1458545]
}
df_states = pd.DataFrame(data)

# a) Print complete information
print("--- State Information ---")
print(df_states)

# b) State with largest Area
largest_area = df_states.loc[df_states['Area'].idxmax(), 'State']
print(f"\nState with largest Area: {largest_area}")

# c) State with largest Population
largest_pop = df_states.loc[df_states['Population'].idxmax(), 'State']
print(f"\nState with largest Population: {largest_pop}")

# d) Calculate Population Density (Density = Population / Area)
df_states['Density'] = df_states['Population'] / df_states['Area']
print("\n--- Report with Population Density ---")
print(df_states)

# e) State with highest population density
highest_density = df_states.loc[df_states['Density'].idxmax(), 'State']
print(f"\nState with highest Population Density: {highest_density}")