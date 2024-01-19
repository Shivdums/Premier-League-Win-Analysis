import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Read the CSV file
path1 = 'La Liga.csv'
football_data = pd.read_csv(path1, index_col=0)
print(football_data.info())

# Print unique values in the 'FT' column
print(football_data['FT'].unique())

# Extracting the scores from the 'FT' column
scores = football_data['FT'].str.split('-', expand=True)
print(scores)

# Rename the columns for clarity
scores.columns = ['Team1', 'Team2']

# Convert the columns to numeric values, handle errors with 'coerce'
football_data[['Team1', 'Team2']] = scores.apply(pd.to_numeric, errors='coerce')

# Create a new column 'Outcome' based on the comparison
football_data['Outcome'] = football_data.apply(lambda row: row['Team 1'] if row['Team1'] > row['Team2'] else (row['Team 2'] if row['Team1'] < row['Team2'] else 'Draw'), axis=1)

# Print the modified DataFrame
print(football_data[['Team1', 'Team2', 'FT', 'Outcome']])
print(football_data.head(15))

win_data = football_data[football_data['Outcome'] != 'Draw']

# Count the number of wins for each team
win_counts = win_data['Outcome'].value_counts()
print(win_counts)
plt.figure(figsize=(8, 8))
plt.pie(win_counts, labels=win_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Wins Distribution for Each Team')
plt.show()