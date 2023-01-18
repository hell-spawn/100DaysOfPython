"""Immutable String"""

title = "Recipe 5: Rewriting, and the Immutable String"
#title[8] = '' # >>> Throws error

#Slicing a piece of a string
colon_position = title.index(':')
discard, post_colon = title[:colon_position], title[colon_position+1:] # 
print(discard) # 'Recipe 5'
print(post_colon) # ' Rewriting, and the Immutable String'

# Partition
pre_colon_text, _, post_colon_text = title.partition(':')
print(pre_colon_text) # 'Recipe 5'
print(post_colon_text) # ' Rewriting, and the Immutable String'

#Updating a string with a replacement

post_colon_text = post_colon_text.replace(' ', '_')
post_colon_text = post_colon_text.replace(',', '_')
print(post_colon_text) # '_Rewriting__and_the_Immutable_String'

# Alternative
from string import whitespace, punctuation

for character in whitespace + punctuation:
    post_colon_text = post_colon_text.replace(character, '_')

print(post_colon_text) # '_Rewriting__and_the_Immutable_String'

#Removing extra punctuation marks
post_colon_text = post_colon_text.strip('_')
print(post_colon_text) # remove leading and trailing _ characters. 
while '__' in post_colon_text:
    post_colon_text = post_colon_text.replace('__', '_') # 

print(post_colon_text)

# Show immutable string
print(id(post_colon_text)) # id = 123XXXXXX
post_colon_text = post_colon_text.replace('_','-')
print(id(post_colon_text)) # id = 456XXXXX

# Tip copy string
other_title = title[:]
print(other_title)
print(title)
print(id(other_title))
print(id(title))

# Other methods string

print('some word'.isnumeric()) # False
print('1298'.isnumeric()) # True
post_colon_text = post_colon_text.lower() 
print(post_colon_text)
