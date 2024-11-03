'''a file is data store in a storage device.
There are two types of files : 1] text file  2] binary file
If we are not specifying any mode during open the file by default it will open the fine in read mode always. 
There are lot of functions for reading , updating , writing , deleting the files.'''

# File creation:

file = open('Sample.txt','r') #open the file in read mode
data = file.read()   # to read the content from the file
#data = file.read(5)  '''''We can also specify how many character we want to read ...
print(data)           # print the data from the file
file.close()    # close the file

