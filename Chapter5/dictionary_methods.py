'''There are various methods of dictionary manipulation .'''

myDict = { 'name':'Falguni',
'profession':'A coder' ,
'Marks':'100' ,
'list':[1,2,3],
'anotherDict':{'college':'Nagpur Institute of Technology',
              'location':'Nagpur',
              'State':'Maharashtra'}
}

print("----:DICTIONARY ITEMS() METHOD:----")
print(myDict.items())  # it gives all the items or (key:value) tuple of dictionary.

print("----:DICTIONARY KEYS() METHOD:----")
print(myDict.keys())   # it gives list of keys in a dict.
'''or'''
print(list(myDict.keys())) 

print("----:DICTIONARY Values() METHOD:----")
print(myDict.values()) # it gives the list of values in a dict.
'''or'''
print(list(myDict.values())) 

print("----:DICTIONARY UPDATE() METHOD:----")
updateDict ={'lovish':'me',
             'Ravi':'junior',
             'profession':'a singer'} # it update a profession key with a singer by removing a coder.
myDict.update(updateDict)  #update the dictionary by adding key-value pairs from updateDict.
print(myDict) 

print("----:DICTIONARY get() METHOD:----")
print(myDict.get('name')) # it gives the corresponding value from dict.
'''or'''
print(myDict['name']) # it gives the corresponding value from dict.

'''difference is:-------->'''

print(myDict.get('name2')) # it does not gives the corresponding value from dict rather than showing error msg it will return 'NONE' value.
'''or'''
print(myDict['name2']) # it does not gives the corresponding value from dict. it will throw an error msg.

