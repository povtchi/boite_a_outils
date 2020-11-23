class NLPPreprocessor:
    def __init__(self):
        # Find the absolute path for the root dir (04-Decision-Science)
        # Uses __file__ as absolute path anchor
        # root_dir = os.path.dirname(os.path.dirname(__file__))
        return self
    def punctuation_remover(self, text):
        # function that removes punctuation from a given text
        import string
        for punctuation in string.punctuation:
            text = text.replace(punctuation, '')
        return text
    def to_lowercase(self, text):
        # function that makes all text lowercase
        return text.lower()
    def num_remover(self, text):
        # removes numbers from a given text
        text = ''.join(char for char in text if not char.isdigit())
        return text
    def stopword_remover(self, text):
        # removes stopwords from given text and returns text as list of words
        # imports
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize
        # english stopwords stored in variable stop_words
        stop_words = set(stopwords.words('english'))
        # splits text into list of words
        word_tokens = word_tokenize(text)
        # removes stopwords from text
        text_list = [word for word in word_tokens if not word in stop_words]
        # returns list of non-stopwords
        return text_list
    def lemmatizer(self, text_list):
        # replaces words in text by their root
        # imports
        from nltk.stem import WordNetLemmatizer
        # instance
        lemmatizer = WordNetLemmatizer()
        # replaces each word in list by its root word
        text_list = [lemmatizer.lemmatize(word) for word in text_list]
        # returns list of each word rooted
        return text_list
    def list_concat(self, text_list):
        # converts list of words back into string
        text = ' '.join(text_list)
        return text
    def preprocessor(self, df_series):
        # complete preprocess with all functions above
        df_series = df_series.apply(punctuation_remover)
        df_series = df_series.apply(to_lowercase)
        df_series = df_series.apply(num_remover)
        df_series = df_series.apply(stopword_remover)
        df_series = df_series.apply(lemmatizer)
        df_series = df_series.apply(list_concat)
        return df_series
