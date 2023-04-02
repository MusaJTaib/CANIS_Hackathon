import pandas as pd

# Load the CSV data into a Pandas DataFrame
df = pd.read_csv('Preprocessed_EXTRA_RussianPropagandaSubset.csv')

# Extract the text column
text_col = df['text']

# Define the number of levels and max number of children
n_levels = 4
max_children = 5

# Split the text into words and count their frequency
words = text_col.str.split(expand=True).stack().value_counts()

# Select the top 5 most frequent words
top_words = words.head(5).index.tolist()

df['text'].fillna('', inplace=True)
# Group the rows by the top words and take the first 5 rows of each group
groups = df.groupby(text_col.str.findall('|'.join(top_words)).apply(lambda x: tuple(sorted(x)))).head(max_children)

# Reset the index and rename the columns
groups = groups.reset_index(drop=True)
groups.columns = ['name', 'value']

# Save the result as a JSON file
groups.to_json('hierarchy.json', orient='records')


import json

# load the hierarchical JSON data from file
with open('hierarchy.json', 'r') as f:
    data = json.load(f)

# convert the hierarchical JSON array to a hierarchical JSON object (dictionary)
root = {"name": "root", "children": []}

for group in data:
    current = root
    for name in group['name'].split('/'):
        match = next((child for child in current['children'] if child['name'] == name), None)
        if not match:
            match = {"name": name, "children": []}
            current['children'].append(match)
        current = match
    current['size'] = group['size']

# save the hierarchical JSON object (dictionary) to file
with open('hierarchy_dict.json', 'w') as f:
    json.dump(root, f)
