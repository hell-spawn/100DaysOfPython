text = "Escuela de la vida y otras cosas"
list_of_letter = [ letter.lower() for letter in text if letter.isalpha()] 
list_of_letter.sort()
unique_letters = set(list_of_letter)
list_of_unique_letters = [ (letter, list_of_letter.count(letter)) for letter in unique_letters ] 
print(list_of_unique_letters.sort(key= lambda x: x[1], reverse=True));
print(list_of_unique_letters)
