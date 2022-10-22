# We are creating simple Spelling Detector

from lib2to3.pytree import convert
from textblob import TextBlob
def Convert(string):
    pan=list(string.split())
    return pan
pan1= input("enter your word: ")
words=Convert(pan1)
corrected=[]
for i in words:
    corrected.append(TextBlob(i))
print("Wrong words: ", words)
print("Corrected words are: ")
for i in corrected:
    print(i.correct(), end=" ")
