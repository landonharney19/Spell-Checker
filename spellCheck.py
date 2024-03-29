from textblob import TextBlob

wordInputList = ["Penos", "Angur"]
correctedWords = []

for i in words:
  correctedWords.append(TextBlob(i))

print("Words with error: ", wordInputList)
print("Fixed words: ")

for i in correctedWords:
  print(i.correct(), end = "")
  
