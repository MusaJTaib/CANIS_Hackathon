import spacy
import pandas as pd
import csv


# Load the English language model in spaCy
nlp = spacy.load('en_core_web_sm')

# Define a text to analyze
# Load the dataframe
df = pd.read_csv('Preprocessed_Dataset_Misinfo_FAKE.csv')

# Concatenate all strings in the dataframe
text = ' '.join(df["text"].astype(str).values.flatten())

# Apply the nlp pipeline to the text
doc = nlp(text)

# Iterate over each entity in the document and print its label and text
for ent in doc.ents:
    print(ent.label_, ent.text)

with open('ner_FAKE.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Label', 'Text'])
    for ent in enumerate(doc.ents):
        writer.writerow([ent.label_, ent.text])
