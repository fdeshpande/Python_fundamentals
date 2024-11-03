''' Repet 3rd program for a list of such words to be sencord: '''

words = ['donkey','pagal','bewkuf','dhaposlebaj']
with open("donkey.txt",'r') as f:
    u = f.read()
for word in words:    
    u = u.replace('word','######')

    with open("donkey.txt",'w') as f:
        f.write(u)
        