import pandas as pd

# Read in the text file
df = pd.read_csv('TOP100_sorted_entities_Misinfo_FAKE.txt', sep=',', header=None, names=['Entity', 'Name', 'Count'])

# Convert the Count column to numeric data type
df["Count"] = pd.to_numeric(df["Count"])

# Write dataframe to CSV file
df.to_csv('TOP100_sorted_entities_Misinfo_FAKE.csv', index=False, sep=',')


df = pd.read_csv('TOP100_sorted_entities_Misinfo_TRUE.txt', sep=',', header=None, names=['Entity', 'Name', 'Count'])

# Convert the Count column to numeric data type
df["Count"] = pd.to_numeric(df["Count"])
# Write dataframe to CSV file
df.to_csv('TOP100_sorted_entities_Misinfo_TRUE.csv', index=False, sep=',')

df = pd.read_csv('TOP100_sorted_entities_RussianPropagandaSubset.txt', sep=',', header=None, names=['Entity', 'Name', 'Count'])

# Convert the Count column to numeric data type
df["Count"] = pd.to_numeric(df["Count"])
# Write dataframe to CSV file
df.to_csv('TOP100_sorted_entities_RussianPropagandaSubset.csv', index=False, sep=',')