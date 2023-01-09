a= "Hello this Is an Example With cased letters"
words = [word.lower() for word in a.split()]
words.sort()
print("The sorted words are:")
for word in words:
   print(word)
