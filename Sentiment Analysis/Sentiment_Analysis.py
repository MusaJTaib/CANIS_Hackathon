import pandas as pd
from textblob import TextBlob
import nltk
import re
nltk.download('all')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob.wordnet import Synset

from nltk import pos_tag
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from sklearn.feature_extraction.text import CountVectorizer
import string

# Reading the CSV file here
data = pd.read_csv('Preprocessed_EXTRA_RussianPropagandaSubset.csv', sep=',', header=0,  names=["index", "text"])

# Showing first 5 lines of the data
# pd.set_option('max_colwidth', 100)
# print(data.head())
# print(data.iloc[5, 1])


# Getting the polarity score and subjectivity score
def get_textblob_sentiment(text):
    print(text)
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity


# Getting polarity and subjectivity for read data
data['blob_polarity'], data['blob_subjectivity'] = zip(*data.iloc[:, 1].apply(get_textblob_sentiment))

# data.head()
# print(data.head())


# Getting polarity scores using Vader
def get_vader_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    return scores['compound']


# get vader sentiment score
data['vader_score'] = data.iloc[:, 1].apply(get_vader_sentiment)

data.head()
print("Getting vader sentiment score")

positive_synsets = Synset('good.a.01').lemmas()
negative_synsets = Synset('bad.a.01').lemmas()

positive_words = [lemma.name() for lemma in positive_synsets]
negative_words = [lemma.name() for lemma in negative_synsets]

# analyzer = SentimentIntensityAnalyzer()
# positive_words = analyzer.lexicon.get('positive')
# negative_words = analyzer.lexicon.get('negative')


# positive_words = ['happy', 'joy', 'love', 'great']
# negative_words = ['angry', 'hate', 'sad', 'bad']
positive_shifters = ['although', 'but', 'despite', 'even though', 'however', 'nonetheless', 'regardless', 'still', 'though', 'yet']
negative_shifters = ['albeit', 'although', 'despite', 'even though', 'however', 'in spite of', 'nevertheless', 'nonetheless', 'though', 'while', 'yet']


# Customized sentiment scoring
def classify_sentiment(text):
    # Remove special characters and lowercase the text
    text = re.sub('[^a-zA-Z0-9\s]', '', text)
    text = text.lower()

    # tokenize
    words = nltk.word_tokenize(text)

    # Initialize sentiment score
    sentiment_score = 0

    # Look for sentiment-shifters and adjust sentiment score
    for i in range(len(words)):
        if words[i] in positive_shifters and i+1 < len(words) and words[i+1] in negative_words:
            sentiment_score -= 1
        elif words[i] in negative_shifters and i+1 < len(words) and words[i+1] in positive_words:
            sentiment_score += 1
        elif words[i] in positive_words:
            sentiment_score += 1
        elif words[i] in negative_words:
            sentiment_score -= 1

    # Classify sentiment based on sentiment score
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'


# Vader sentiment scoring
def vader_analysis(text):
    sid = SentimentIntensityAnalyzer()
    vader_score = sid.polarity_scores(text)['compound']
    if vader_score > 0:
        vader_sentiment = 'positive'
    elif vader_score < 0:
        vader_sentiment = 'negative'
    else:
        vader_sentiment = 'neutral'
    # print("Vader: ", vader_sentiment)

    # Look for sentiment-shifters and adjust sentiment score
    words = nltk.word_tokenize(text)
    for i in range(len(words)):
        if words[i] in positive_shifters and i + 1 < len(words) and words[i + 1] in negative_words:
            vader_score -= 1
        elif words[i] in negative_shifters and i + 1 < len(words) and words[i + 1] in positive_words:
            vader_score += 1
        elif words[i] in positive_words:
            vader_score += 1
        elif words[i] in negative_words:
            vader_score -= 1
    # Custom sentiment analysis
    # custom_sentiment = classify_sentiment(sentence)
    # print("Custom: ", custom_sentiment)
    return vader_score


data['vader_score'] = data.iloc[:, 1].apply(vader_analysis)
data['vader_sentiment'] = data.loc[:, 'vader_score'].apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')
data.to_csv("sentiment_analysis.csv")
