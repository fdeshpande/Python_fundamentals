'''We can also use f.readline() function to read on full line at a time .'''

file = open('Sample.txt','r') #open the file in read mode
# read first line
data = file.readline()   
print(data)    # print the data from the file
# read second line
data = file.readline()   
print(data)
# read third line
data = file.readline()   
print(data)
# read fourth line  and so on...
data = file.readline()   
print(data)
file.close()    # close the file
