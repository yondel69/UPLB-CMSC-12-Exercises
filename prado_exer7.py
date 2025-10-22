'''
Dandel Oliver S. Prad
2025-01061
CMSC 12 G-6L

- saveCatalogue and loadCatalogue function
- Each book is saved in the books.dat file with the format: <book_code>|<title>|<author>|<price>|<date>|<status>|<status>|<notes>
'''

def saveCatalogue(catalogue):
    with open("books.dat","w") as f: # .close() is redundant when using with open() 
        #correction, "w" instead of "a" when saving
        #iterates through each book in the catalogue
        for book_code, book_information in catalogue.items():
            print(f"Added {book_code} ({book_information[0]} by {book_information[1]}) to books.dat")
            f.write(f"<{book_code}>|<{book_information[0]}>|<{book_information[1]}>|<{book_information[2]}>|<{book_information[3]}>|<{book_information[4]}>|<{book_information[4]}>|<{book_information[5]}>\n")
    print("\nSuccessfully saved the book catalogue!!")

def loadCatalogue(catalogue): 
    #Loads the book catalogue from books.dat file and adds it to the main program dictionary
    #Each line from the file is split by '|' and stored in the dictionary.
    with open("books.dat","r") as f:
        print("Successfully loaded the book catalogue containing:")
        for line in f:
            book_info = line.strip().split("|") #removes whitespace and '|'
            book_code = book_info[0]
            catalogue[book_code] = book_info[1:]
            print(f"{book_info[0]} ({book_info[1]} by {book_info[2]})")
       