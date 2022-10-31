# text-mining

Please read the [instructions](instructions.md).

1. Project Overview
For this project, I choose to use the datasource of gutenburg in the purpose of analyzing the text. I got to know different types of toolkits such as nltk and the fuzz tp generate analysis with methods other than what we did in class. I am hoping to create an overview of the book's text and compar it to another book written by the same author.

2. Implementation
I choose to use the famous novel "the Call of the Wild" by American writer Jack London. The analysis is based mainly on its text decomposed into words. In my code, I computed the frequency of each word appeared in the novel and tested the sentiment of the text in terms of the tone. Also, I counted the total number of words and distinctive words. What's more, I tested on the similaritu in percentage between the Call of the Wild and White Fang which were both written by Jack London regarding how many of their vocabularies are overlapped. Overall, it provides a general idea on the text breakdown of the book.

3. Results
Output from the Terminal:

Total number of words: 161009

Number of different words: 13945

The top 20 most common words appears in the book are:
the      9643
and      5263
of       3957
to       3909
a        3728
in       2405
his      2350
he       2300
was      1767
that     1727
with     1613
it       1517
you      1415
as       1309
said     1230
had      1216
i        1169
for      1135
mr       1067
him      1005

The result of similarity test between two books of the same author is:
39

Following is the result of sentiment analysis:
{'neg': 0.092, 'neu': 0.784, 'pos': 0.124, 'compound': 1.0}

Interestingly, the similarity of those two book by the same author is not very high. Anf according to the sentiment analysis, the result is tilted more towards positive side. It makes sense since this book tells a relatively inspirational story. Also, we can tell the book is written in the third perspective since the words "he", "him", and "his" all appear frequently.

4. Reflection
From a process point of view, firstly, I think there should be more tools that could be used for analyzing, especially on the comparison between two book. Secondly, I think more visual tools could be applied in this situation, otherwise the result might seem a bit too simple and abstract to understand. Last but not least, I think my preparation for this project is not sufficient enough, and I might need to spend more time to make it mor logical more than just simply looking at the text breakdown. Overall, through this assignment, I had a thourough understanding of the process of analysis on python and got familiar with the code and tools.
