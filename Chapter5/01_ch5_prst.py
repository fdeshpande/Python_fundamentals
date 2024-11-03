# Write a program to create a dict of hindi words with values as their english translation 
# provide user with an option to look it up!

hindiengDict = {'computer':'sanganak',
                'table':'mej',
                'mouse':'chuha',
                'write':'likhna',
                'read':'padhna'
}
print("options are",hindiengDict.keys())
a = input("Enter the english word\n")
print("The meaning of your word is",hindiengDict.get(a))