'''Write a program to find out the line number where python is present from que 5: '''

u = True
i = 1
with open('log.txt') as f:
    
    while u :
        u =f.readline()

        if 'python' in u:
            print(u)
            print("python is present")
            print(i)
        i = i+1    
        
        
    

    

         
 