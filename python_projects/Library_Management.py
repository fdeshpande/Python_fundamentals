class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in the library are: \n")
        for book in self.books:
            print("\t"+book)

    def borrow(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)

        else:
            print("sorry this book has been issued by someone or may be not available in the library. Kindly wait till we received from him/her.")

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it . Have a great day ahead!!")



class Student:
    def requestBook():
        book = input("Enter the book which one you want to borrow: \t")
        return book

    def returnBook():
        book = input("Enter which book you want to return :\t")
        return book    


if __name__ =="__main__":
    s = Student()
    centralLibrary = Library(["Algorithms","Django","C -programming","Object Oriented Programming","Basics of java ","Data Structure"])
    while (True):
        welcomeMsg = '''======================Welcome to central Library====================\n
        Please choose an option:
        1. Listing all the books.
        2. Request a book.
        3. Add/Return a book.
        4. Exit the library.'''

        print(welcomeMsg)

        a = int(input("Enter your choice :\t"))

        if a==1:
            centralLibrary.displayAvailableBooks()

        elif a==2:
            centralLibrary.borrow(Student.requestBook())

        elif a == 3:
            centralLibrary.returnBook(Student.returnBook())
            
        elif a == 4:
            print("Thanks for choosing Central Library ! Have a great day ahead!!")
            exit()

        else:
            print("Invalid Choice!!!") 


