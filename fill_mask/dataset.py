from transformers import AutoTokenizer
 
from collections import defaultdict

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
 
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))


COUNT_OF_WORDS_TO_REMOVE = 10

def get_dictionary(text):
    word_freqs = defaultdict(int)
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    for word in filtered_sentence:
        word_freqs[word] += 1
    return word_freqs 


def get_unique_words(text):
    word_freqs = get_dictionary(text)
    word_freqs_unique = sorted(word_freqs.items(), key=lambda x:x[1])[COUNT_OF_WORDS_TO_REMOVE:]
    unique_words = [key for key,count in word_freqs_unique]
    return remove_punctuations(unique_words)

def remove_punctuations(input_list):
    new_list = []
    for word in input_list:
        if word in string.punctuation:
            continue
        new_list.append(word)
    return new_list



