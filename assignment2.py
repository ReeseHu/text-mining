import urllib.request
import pprint
import string
from multiprocessing.sharedctypes import Value
from optparse import Values
import json



def get_file():
    """
    Returns a sorted list of town names
    """
    url = f'https://www.gutenberg.org/files/730/730-0.txt'
    with urllib.request.urlopen(url) as f:
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
    return text
    
# print(get_file())


####Characterizing by Word Frequencies

def process_word():
    """Makes a histogram that contains the words from a file and its corresponding frequency.
    """
    
    hist = {}
    text = get_file()
    strippables = string.punctuation + string.whitespace

   
    for word in text.split():
        
        word = word.replace('-', ' ')

        word = word.strip(strippables)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1

    return hist

# print(process_word())



####Computing Summary Stats

def most_common(hist):
    """
    It return the list of words with descending frequency.
    """
    t = list()
    hist=dict(hist)
    for word, frequency in hist.items():
        t.append((frequency,word))
    t.sort(reverse=True)
    return t

def top_common(hist,n):
    """
    It gives us the top n most frequent words in the text.
    """
    t = most_common(hist)
    for freq, word in t[:n]:
        print(word, '\t', freq)


def total_word(hist):
    """
    This function return the total number of words in this book.
    """
    total = 0
    for freq in hist.values():
        total += freq
    return total


def different_words(hist):
    """
    This function returns the number of different vocabulary in this book
    """
    return len(hist)

    


#####Natural Language Processing
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_analysis(text):
    """
    This function analyze the sentiment of the text.
    """

    text = str(text)
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    return score




from thefuzz import fuzz

def get_another_book():
    """
    Returns a sorted list of town names
    """
    url = f'https://www.gutenberg.org/cache/epub/910/pg910.txt'
    with urllib.request.urlopen(url) as f:
        response = urllib.request.urlopen(url)
        data = response.read()
        book = data.decode('utf-8')
    return book

def similarity_analysis():
    '''
    This function return the extent of similarity between two books of Jack London, the Call of the Wild and White Fang.
    '''
    text = str(get_file())
    book = str(get_another_book())

    return fuzz.ratio(text,book)




def main():

    hist = process_word()
    # print(most_common(hist))

    # print('Total number of words:', total_word(hist))
    # print('Number of different words:', different_words(hist))
    
    print('The top 20 most common words appears in the book are:')
    top_common(hist,20)
    
    # text = get_file()
    # print('Following is the result of sentiment analysis:')
    # print(sentiment_analysis(text))

    # print('The result of similarity test between two books of the same author is:')
    # print(similarity_analysis())
    

    # text = get_file()
    # print('Following is the result of sentiment analysis:')
    # sentiment_analysis(text)


if __name__ == '__main__':
    main()

    




