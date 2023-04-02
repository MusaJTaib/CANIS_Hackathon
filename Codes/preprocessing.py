import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # Lemmatize text
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    # Join lemmas back into a single string
    preprocessed_text = ' '.join(lemmas)
    return preprocessed_text

print("Starting")
df = pd.read_csv("./data/DataSet_Misinfo_FAKE.csv", index_col=[0])
df["text"] = df["text"].astype(str)
df["text"] = df["text"].apply(preprocess_text)
df.to_csv("Preprocessed_Dataset_Misinfo_FAKE.csv")


df = pd.read_csv("./data/DataSet_Misinfo_TRUE.csv", index_col=[0])
df["text"] = df["text"].astype(str)
df["text"] = df["text"].apply(preprocess_text)
df.to_csv("Preprocessed_Dataset_Misinfo_TRUE.csv")

df = pd.read_csv("./data/EXTRA_RussianPropagandaSubset.csv", index_col=[0])
df["text"] = df["text"].astype(str)
df["text"] = df["text"].apply(preprocess_text)
df.to_csv("Preprocessed_EXTRA_RussianPropagandaSubset.csv")
