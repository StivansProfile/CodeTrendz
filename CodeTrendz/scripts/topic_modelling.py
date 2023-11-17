import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from gensim import corpora, models
import pyLDAvis.gensim_models
import matplotlib.pyplot as plt
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")


class TopicModelling:
    def __init__(self, data):
        self.data_objects = data

    def start_modelling(self):
        df = pd.DataFrame(self.data_objects)

        # Text preprocessing --------------------------

        stop_words = set(stopwords.words("english"))
        lemmatizer = WordNetLemmatizer()

        def preprocess_text(text):
            tokens = word_tokenize(text.lower())
            tokens = [
                lemmatizer.lemmatize(token)
                for token in tokens
                if token.isalnum() and token not in stop_words
            ]
            return tokens

        df["tokens"] = df["description"].apply(preprocess_text)

        # Dictionary and corpus creation ----------------------

        # Create a dictionary representation of the job descriptions
        dictionary = corpora.Dictionary(df["tokens"])

        # Create a bag-of-words corpus
        corpus = [dictionary.doc2bow(tokens) for tokens in df["tokens"]]

        # Train an LDA model ---------------------
        lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

        # Visualize the topics
        vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
        # pyLDAvis.enable_notebook()
        pyLDAvis.save_html(vis, "./data/vis_data.html")
