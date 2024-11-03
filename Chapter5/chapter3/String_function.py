'''String functions are generally used to manipulate the string
there are various type of string manipulation functions'''

story = 'I am Falguni Deshpande and today i started learning python and harry who is a youtuber'
print(len(story)) # It returns the length of story. 
print(story.capitalize()) # This function capitalize the first letter from the string.
print(story.count('a')) # mostly this function is used to count the characters. 
print(story.count('and')) 
print(story.endswith('youtuber')) # this function checks the word whether it is ending with the given string. 
print(story.find('and')) # This function finds a word and returns the index of first occurance of that word in the string.
print(story.replace('Falguni','Fuggi')) # This function replace the old word by the new word.


