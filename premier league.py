import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
path1= 'Premier league.csv'
football_data = pd.read_csv(path1, index_col=0)
print(football_data.head())
print(football_data.dtypes)
print(np.unique(football_data['FT']))
print(football_data.info())

# Create an array to store outcomes
outcomes = np.full(len(football_data), 'Draw', dtype='object')

def determine_outcome(row):
    scores = [int(s) for s in str(row['FT']).split('-')]
    if scores[1] > scores[0]:
        return 'Win'
    elif scores[0] < scores[1]:
        return 'Loss'
    else:
        return 'Draw'


football_data['Outcome'] = outcomes

# Print the modified DataFrame
print(football_data[['Team 1', 'Team 2', 'FT', 'Outcome']])



plt.hist(football_data["FT"], color= "green", edgecolor="white", bins=2)
plt.title("Histogram of FT vs Frequency")
plt.xlabel("FT")
plt.ylabel("Frequency")
plt.show()

football_data.dropna(axis=0, inplace=True)
plt.scatter(football_data['Date'], football_data['FT'], c='violet')
plt.title("Scatter plot of Date vs FT")
plt.xlabel("Date")
plt.ylabel("FT")
# Rotate y-axis labels
plt.yticks(rotation=45)
plt.show()

sns.histplot(football_data["FT"])
plt.xticks(rotation=60)
plt.show()

sns.countplot(x="Team 1", data=football_data, hue='FT', palette="deep")
plt.xticks(rotation=60)
plt.show()

sns.boxplot(x= football_data['Team 1'], y= football_data['Team 2'], hue=football_data['Date'])
plt.xticks(rotation=60)
plt.show()