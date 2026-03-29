import matplotlib.pyplot as plt
import pandas as pd

# 1. Creating the dataset
data = {
    'Company': ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS Origin', 'Amdocs'],
    'New_Recruitments': [2500, 3100, 2800, 1500, 1900, 2200, 1200, 1100]
}
df = pd.DataFrame(data)

# a) Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df['Company'], df['New_Recruitments'], color='skyblue')
plt.title('New Recruitments by Company')
plt.xticks(rotation=45)
plt.ylabel('Number of Employees')
plt.show()

# b & c) Customized Pie Chart
# Adding 'explode' to highlight the top recruiter (Google)
explode = [0, 0.1, 0, 0, 0, 0, 0, 0] 
plt.figure(figsize=(8, 8))
plt.pie(df['New_Recruitments'], labels=df['Company'], autopct='%1.1f%%', explode=explode, shadow=True)
plt.title('Recruitment Distribution (Customized)')
plt.show()

# d) Doughnut Chart
plt.figure(figsize=(8, 8))
plt.pie(df['New_Recruitments'], labels=df['Company'], autopct='%1.1f%%', pctdistance=0.85)
# Draw a white circle at the center to make it look like a doughnut
center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)
plt.title('Recruitment Doughnut Chart')
plt.show()

# Compare IBM & Amdocs
compare_df = df[df['Company'].isin(['IBM', 'Amdocs'])]
plt.bar(compare_df['Company'], compare_df['New_Recruitments'], color=['blue', 'orange'])
plt.title('Comparison: IBM vs Amdocs')
plt.show()