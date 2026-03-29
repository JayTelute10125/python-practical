import pandas as pd

# Creating dummy data for demonstration (you can skip this if you have the file)
data = {
    'title': ['Python Basics', 'Data Science 101', 'Intro to AI', 'Pandas Pro', 'Java Expert'],
    'author': ['John Smith', 'Alice Doe', 'John Smith', 'Bob Brown', 'Alice Doe'],
    'edition': [1, 3, 2, 1, 4],
    'pub_year': [2020, 2022, 2018, 2021, 2015],
    'pub_house': ['OReilly', 'Pearson', 'OReilly', 'Packt', 'Pearson'],
    'price': [450, 600, 550, 400, 700]
}
pd.DataFrame(data).to_csv('books.csv', index=False)

# Main Script
df = pd.read_csv('books.csv')

# a) Print the complete report in Tabular form
print("--- Complete Book Report ---")
print(df.to_string())

# b) Print list of books of a given author
target_author = "John Smith"
print(f"\n--- Books by {target_author} ---")
print(df[df['author'] == target_author])

# c) Print list of books of a given publishing house
target_pub = "Pearson"
print(f"\n--- Books published by {target_pub} ---")
print(df[df['pub_house'] == target_pub])

# d) Titles of cheapest & costliest book
cheapest = df.loc[df['price'].idxmin(), 'title']
costliest = df.loc[df['price'].idxmax(), 'title']
print(f"\nCheapest Book: {cheapest}")
print(f"Costliest Book: {costliest}")

# e) Sort by year of publication
print("\n--- Books Sorted by Publication Year ---")
print(df.sort_values(by='pub_year'))