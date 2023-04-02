import pandas as pd
from collections import Counter
import csv

# Load the dataframe
df = pd.read_csv('Preprocessed_Dataset_Misinfo_FAKE.csv')

# Concatenate all strings in the dataframe
all_text = ' '.join(df["text"].astype(str).values.flatten())

# Split the text into individual words
words = all_text.split()

# Count the frequency of each word
word_counts = Counter(words)

# Get the top 50 words with their count
top_50_words = word_counts.most_common(50)

# Print the top 50 words with their count
for i, (word, count) in enumerate(top_50_words):
    print(f"{i+1}. {word}: {count}")

with open('top_words_FAKE.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Word', 'Count'])
    for word, count in enumerate(top_50_words):
        writer.writerow([word, count])
