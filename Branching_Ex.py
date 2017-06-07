sentence = "The quick brown fox jumped over the lazy dogs"
longest = ""
words = sentence.split()

for word in words:
    if len(word) > len(longest):
        longest = word
print ("The word '" + longest + "' is ", len(longest), " characters long.")
