# text-mining



# Project Overview

For this project, I choose to use the datasource of gutenburg in the purpose of analyzing the text. I got to know different types of toolkits such as nltk and the fuzz tp generate analysis with methods other than what we did in class. I am hoping to create an overview of those books text and cross compare them to other book written by the same author.

# Implementation

I choose to use the famous novel "the Call of the Wild" by American writer Jack London for demonstration. I stored six books in the data file which are the top six most read book by Jack London for cross comparison. The analysis is based mainly on its text decomposed into words. In my code, I computed the frequency of each word appeared in the novel and tested the sentiment of the text in terms of the tone. Also, I counted the total number of words and distinctive words. What's more, I tested on the extent of similarity in percentage between two books, the Call of the Wild and White Fang in demonstration, which were both written by Jack London regarding how many of their vocabularies are overlapped. Overall, it provides a general idea on the text breakdown of the book.

# Results

1. For the book the Call of the Wild:


Total number of words: 31821

Number of different words: 5051


The top 20 most common words appears in the book are:
the      2274

and      1530

of       871

he       813

was      697

to       676

a        655

his      559

in       537

it       367

buck     306

with     304

that     302

him      288

they     285

had      274

as       256

for      237

on       225

were     217



Following is the result of sentiment analysis:

{'neg': 0.117, 'neu': 0.786, 'pos': 0.097, 'compound': -1.0}

2. for White Fang

Total number of words: 72180

Number of different words: 7454

The top 20 most common words appears in the book are:

the      5151

and      2990

he       2203

of       2182

to       1755

was      1731

his      1582

a        1433

in       1210

him      969

it       885

that     836

had      817

with     640

white    635

but      526

fang     525

at       500

on       473

for      448

Following is the result of sentiment analysis for White Fang:

{'neg': 0.124, 'neu': 0.776, 'pos': 0.1, 'compound': -1.0}


The result of similarity test between two books of the same author is:
54

Interestingly, the similarity of those two book by the same author is not very high, although both of those books tell the story about dogs and their adventures. According to the sentiment analysis, the result is tilted more towards negative side. It makes sense since those book tell inspirational adventurous stories regarding setbacks and difficulties. Also, we can tell both books are written in the third perspective since the words "he", "him", and "his" all appear frequently.



# Reflection

Speaking of the process, firstly, I think there should be more tools that could be used for analyzing, especially on cross comparison between more than two books. Secondly, I think more visual tools could be applied in this situation, otherwise the result might seem a bit too simple and abstract to understand. Last but not least, I think my preparation for this project is not sufficient enough, and I might need to spend more time to find more data andmake it more logical than simply just looking at the text breakdown. Overall, through this assignment, I had a thourough understanding of the procedire of analysis on python and got familiar with the code and tools.
