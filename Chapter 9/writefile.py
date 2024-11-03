'''In order to write a file we open the file in write or append mode.
If open the file in append mode then we write the content at the end 
of the file with staying previously written contents.
If open the file in write mode then we write the content in the file
to overwrite previously written contents.'''

# append mode:
file = open('Sample.txt','a') #open the file in append mode
data = file.write("I am doing good job") # write the content 
print(data)           # print the data from the file
file.close()  

# write mode:
file = open('another.txt','w') #open the file in write mode
data = file.write("I am doing good job") # write the content 
print(data)           # print the data from the file
file.close() 

