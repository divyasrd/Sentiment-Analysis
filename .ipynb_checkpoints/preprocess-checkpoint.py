import nltk
nltk.download('stopwords')   # Stopwords in English
nltk.download('wordnet')   # Vocabulary for Lemmatization
nltk.download('vader_lexicon')   # Lexicon for VADER Model
nltk.download('punkt')   # Tokenizer Rules
nltk.download('punkt_tab') 

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re

def process_review(review):
    # Convert_review into lowercase form
    review_lower = review.lower()

    #Remove punctuations,numbers
    review_punc_nums_removed = re.sub(r"[^a-z\s]","", review_lower)

    # Tokenize the review: convert sentence into words
    reviews_tokens=word_tokenize(review_punc_nums_removed)

    # Remove stopword
    stop_words = stopwords.words('English')
    review_tokens_stopwords_removed = [token for token in reviews_tokens if token not in stop_words]

    # Lemmatization
    lemmatizer= WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token,pos='n') for token in review_tokens_stopwords_removed]

    # Put together all the tokens as as single string object
    return" ".join(lemmatized_tokens)

    if __name__ == "__main__":
        review = "The product was really nice!!!"
        print(process_review(review))