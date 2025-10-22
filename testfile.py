# Dandel Oliver S. Prado
# CMSC 12 G-6L

# Personal library program that manages book informations incuding 
# name, author, price, status, and lets you add reader's notes. 
#------------------------------------------------------------------

def mainMenu():
    print(f"\n=========== MENU ===========",) #menu ui
    print("[1] Add a book")
    print("[2] View all books")
    print("[3] Change book status")
    print("[4] Add note to book")
    print("[5] Remove book")
    print("[6] Clear Book Catalogue")
    print("[0] Exit")
    print("============================")
    #can also be typed as print to condense | the format above was used in this instance to improve readability
    '''print(f"[1] Add a book", "\n[2] View all books", "\n[3] Change book status", 
        "\n[4] Add note to book", "\n[5] Remove book", "\n[6] Clear Book Catalogue", "\n[0] Exit")'''

    while True:
        user_input = int(input(f"Enter Option: "))
        if 0 <= user_input <= 6:
            return user_input
        else:
            print("Invalid option. Please try again.") #corrects the user if user_input is higher than 6

def addBook(catalogue):
    print(f"\n====== ADD A BOOK ====== ")
    book_code = str(input("Book code: "))
    if book_code in catalogue: #avoids redundancy and user error
        print("Book code already exists.")
        return
    #user inputs book_information
    book_name = str(input("Book name: "))
    author = str(input("Author: "))
    price = float(input("Price: "))
    date_bought = str(input("Date Bought: "))
    
    #status check
    while True: 
        status = str(input("Status: ").lower())
        if status in ["to-read", "currently-reading", "finished"]:
            break
        else: #corrects the user
            print("Status can only be 'to-read', 'currently-reading', and 'finished'")
    
    catalogue[book_code] = [book_name, author, price, date_bought, status, []] #0, 1, 2, 3, 4, 5 | [] = notes
    #                           0         1       2         3         4     5
    print("Book has been added!")  

def viewCatalogue(catalogue): 
    print(f"\n======== MY LIBRARY ========")
    if not catalogue: #checks if catalogue is empty | if true, the print statement will execute
        print("No books found in your library.")
        print("============================")
        return #exits this function
    
    #if catalague is not empty, this code will run
    for book_code, book_information in catalogue.items(): #catalogue = {book code, (book information_1, book information_2, ...)}
        #loops the code for each book code, prints the book information until the next iteration
        print(f"\n{book_code}")
        print(f"Book name: {book_information[0]}")
        print(f"Author: {book_information[1]}")
        print(f"Price: {book_information[2]}")
        print(f"Date bought: {book_information[3]}")
        print(f"Status: {book_information[4]}")
        print(f"My notes: ")

        if book_information[5]:
            for notes in book_information[5]:
                print(f">>> {notes}") #do not add a break, causes infinite loop | medyo nabobo sa part na to
        else:
            print(f"       No notes yet...") #adds the illusion of being centered
            print()

def loopcheck(catalogue):
    while True:
        book_code = str(input(f"Enter code of book to change its status: "))
            #provides the user the ability to quit this function
        if book_code.lower() == 'quit': 
            print("Exiting operation...")
            return None #exits the function
        if book_code in catalogue:
            return book_code
        else:
            print("Book is not in library. Try again or 'quit' to cancel")

def changeStatus(catalogue):
    print(f"\n======= CHANGE STATUS =======")
    book_code = loopcheck(catalogue, "change its status")
    if book_code is None:  # User chose to quit
        return
    book_information = catalogue[book_code]
    while True: 
        status_types = ["to-read", "currently-reading", "finished"]
        new_book_status = input(f"New status of {book_information[0]} by {book_information[1]}: ").lower() #new status of book_name by author
        #added .lower()  
        if new_book_status in status_types:
            book_information[4] = new_book_status
            print("Status updated.")
            break
        else:
            print("Status can only be set as to-read, currently-reading, and finished. Try again.")    

def addNote(catalogue):
    print(f"\n======= ADD NOTE =======")
    book_code = loopcheck(catalogue, "change its status")
    if book_code is None:  # User chose to quit
        return
            
    book_information = catalogue[book_code]
    reader_notes = str(input(f"Add note to {book_information[0]} by {book_information[1]}: "))
    book_information[5].append(reader_notes)
    print("Added note. :)")

def removeBook(catalogue):
    #i added a confirmation function to remove the possibility of users accidentally deleting their catalogue
    print(f"\n======= REMOVE BOOK =======")
    book_code = str(input(f"Enter code of book to remove it from library: "))
    if book_code not in catalogue:
        print("Book does not exist.")
        return

    book_information = catalogue[book_code]
    clearlib_choice = input(f"Do you want to delete this book from your library? (y/n): ").lower() 
    if clearlib_choice != 'y':
        return
    else:
        del catalogue[book_code]
        print(f"You have deleted {book_information[0]} by {book_information[1]}")
        print("===========================")

def clearLibrary(catalogue):
    #i added a confirmation function to remove the possibility of users accidentally deleting books in their catalogue
    clearlib_choice = input("Do you want to clear all books? (y/n): ").lower() 
    if clearlib_choice != 'y':
        return
    else:
        print(f"\nNo more books in your catalogue. :(")
        print()
        catalogue.clear()

def mainProgram(): #main function 
    catalogue = {"MIBF1": ["Goodbye, Again", "Jonny Sun", 650.0, "09-Sep-2025", "to-read", []], #sample lib
                 "MIBF2": ["The Book", "Anna Cruz", 900.0, "09-Sep-2025", "currently-reading", []] #for testing
                 }

    while True:
        choice = mainMenu()
        if choice == 0: 
            print(f"\nExiting book catalogue...")
            print("Bye!")
            break

        options = {1: addBook, 2: viewCatalogue, 3: changeStatus, 4: addNote, 5: removeBook, 6:clearLibrary} 
        #looks cleaner than 10 if-elif lines
        if choice in options:
            options[choice](catalogue)

mainProgram()