import os
import csv

# Set path for file
txt1path = os.path.join("raw_data", "paragraph_1.txt")
txt2path = os.path.join("raw_data", "paragraph_2.txt")

# Open the txt
f = open(txt1path, "r")
contents = f.read()
f.close()

characters = len(contents)
words = contents.split()
num_words = len(words)
sentence = contents.split(".")
sentq = contents.split("?")
sentex = contents.split("!")
letters_in_words = characters/num_words
num_sent = len(sentence) - 1 + len(sentq) - 1 + len(sentex) - 1
avg_sent_length = num_words/num_sent
#print(characters)
print("Paragraph Analysis")
print("------------------")
print("Approximate word count: " + str(num_words))
print("Approximate sentence count: " + str(num_sent))
print("Average word length: " + str(round(letters_in_words, 2)))
print("Average sentence length: " + str(round(avg_sent_length, 2)))


