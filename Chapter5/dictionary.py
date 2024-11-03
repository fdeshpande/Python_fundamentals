'''Dictionary is a collection of key-value pairs.
it is unodered.
it is mutable.
it is indexed.
Can not contain duplicate keys.
'''
# Syntax:
'''
   a = { 'key': 'value', 'Falguni':'A coder' ,'Marks':'100' ,'list':[1,2,3]}
   
'''
# Creation of Dictionary:

myDict = { 'name':'Falguni','profession':'A coder' ,'Marks':'100' ,'list':[1,2,3]
,'anotherDict':{'college':'Nagpur Institute of Technology','location':'Nagpur','State':'Maharashtra'}}

print(myDict)      # print the full dictionary content.
print(myDict['name'],myDict['profession']) #print name value and profession value.

myDict['Marks']=['89','98'] #Modify the dictionary.
print(myDict['Marks'])
print(myDict['anotherDict']['location']) # printing the value from nested dictionary.