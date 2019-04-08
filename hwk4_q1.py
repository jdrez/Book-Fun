from hwk4_q1_classes import List, Person, Book, BookTree, PersonTree

def printState():
    ''' prints the people and what books they have'''
    curr_person = people.getFront()
    for person in range(people.getSize()):
        print(curr_person.getData().getName() + "'s books: " + curr_person.getData().getBooks().printList("name"))
        curr_person = curr_person.getNext()

people = List()
books = List()

def showFullState():
    ''' gives detailed information about every person (ID, name. age, friends, books, book history
        and every book (ID, title, author, genre, edition, rating, annotated)'''
    curr_node = people.getFront()
    curr_number = 1
    print("People")
    for i in range(people.getSize()):
        print(str(curr_number) + ".\tID: " + str(
            curr_node.getData().getID()) + "\tName: " + curr_node.getData().getName() + "\tAge: " + str(
            curr_node.getData().getAge()) + "\tFriends: " + curr_node.getData().getFriends().printList(
            "name") + "\tBooks: " + curr_node.getData().getBooks().printList(
            "name") + "\tBook History: " + curr_node.getData().getBookHistory().printList("name"))
        curr_node = curr_node.getNext()
        curr_number += 1
    print("\nBooks")
    curr_book_node = books.getFront()
    curr_book_number = 1
    for i in range(books.getSize()):
        print(str(curr_book_number) + ".\tID: " + str(
            str(curr_book_node.getData().getID())) + "\tTitle: " + curr_book_node.getData().getName() + "\tAuthor: " + curr_book_node.getData().getAuthor()
            + "\tGenre: " + curr_book_node.getData().getGenre() + "\tEdition: " + str(curr_book_node.getData().getEdition()) + "\tRating: " +
            str(curr_book_node.getData().getRating()) + "\tAnnotated: <<" + str(curr_book_node.getData().getAnnotation()) + ">> ")
        curr_book_node = curr_book_node.getNext()
        curr_book_number += 1

def eraseTree(tree):
    '''erases the tree'''
    bookNode = books.getFront()
    while bookNode != None:
        bookNode.getData().setLeft(None)
        bookNode.getData().setRight(None)
        bookNode = bookNode.getNext()
    tree.emptyTree()

def sortType(type, version):
    ''' sorts the tree based off of whether it is person or book (version) and what kind the user wants to sort by (type)'''
    if version == "book":
        bookFamily = BookTree()
        eraseTree(bookFamily)
        bookNode = books.getFront()

        while bookNode != None:
            bookFamily.include(bookNode.getData(), type)
            bookNode = bookNode.getNext()

        temp = bookFamily.startOrderedList(type)
        x = temp.getFront()
        while x != None:
            print(x.getData())
            x = x.getNext()

    if version == "person":
        personFamily = PersonTree()
        eraseTree(personFamily)
        personNode = people.getFront()

        while personNode != None:
            personFamily.include(personNode.getData(), type)
            personNode = personNode.getNext()

        temp = personFamily.startOrderedList(type)
        x = temp.getFront()
        while x != None:
            print(x.getData())
            x = x.getNext()

# creating people
viraj = Person("Viraj", 16, people, books)
dang = Person("Dang", 20, people, books)
alex = Person("Alex", 17, people, books)
josh = Person("Josh", 16, people, books)
teddy = Person("Teddy", 15, people, books)
jon = Person("Jon", 25, people, books)
gerald = Person("Gerald", 10, people, books)
bartholomew = Person("Bartholomew", 8, people, books)

# creating books
book1 = Book("The Glass Castle", "Jeanette Walls", "memoir", 1, books)
book2 = Book("Fahrenheit 451", "Ray Bradbury", "dystopian", 1, books)
book3 = Book("A Brief History of Time", "Stephen Hawking", "non-fiction", 1, books)
book4 = Book("The Martian", "Andy Weir", "science fiction", 1, books)
book5 = Book("Artemis", "Andy Weir", "science fiction", 1, books)
book6 = Book("The Da Vinci Code", "Dan Brown", "mystery", 1, books)
book7 = Book("Angels and Demons", "Dan Brown", "mystery", 1, books)
book8 = Book("The Kite Runner", "Khaled Hosseini", "drama", 1, books)
book9 = Book("The Great Gatsby", "F. Scott Fitzgerald", "drama", 1, books)
book10 = Book("To Kill A Mockingbird", "Harper Lee", "historical fiction", 1, books)
book11 = Book("Romeo and Juliet", "William Shakespeare", "romantic drama", 1, books)
book12 = Book("The Odyssey", "Homer", "mythology", 1, books)
book13 = Book("The Catcher in the Rye", "J.D. Salinger", "drama fiction", 1, books)

# adding friends
viraj.addFriend(dang)
viraj.addFriend(alex)
viraj.addFriend(josh)
viraj.addFriend(teddy)
viraj.addFriend(bartholomew)
dang.addFriend(viraj)
dang.addFriend(teddy)
dang.addFriend(jon)
alex.addFriend(gerald)
alex.addFriend(jon)
alex.addFriend(teddy)
alex.addFriend(viraj)
alex.addFriend(dang)
teddy.addFriend(josh)
josh.addFriend(teddy)
jon.addFriend(gerald)
jon.addFriend(viraj)
jon.addFriend(dang)
gerald.addFriend(teddy)
bartholomew.addFriend(viraj)


# adding books
dang.addBook(book1)
dang.addBook(book2)
dang.addBook(book3)
dang.addBook(book4)
alex.addBook(book5)
viraj.addBook(book6)
viraj.addBook(book7)
josh.addBook(book11)
josh.addBook(book12)
josh.addBook(book13)
bartholomew.addBook(book8)
jon.addBook(book9)
alex.addBook(book10)

medium = input("Do you want to sort using medium brother. If yes: type 'yes'. If no: type anything else. ")
if medium == "yes":
    which_type = input("To sort books: type 'book'. To sort people: type 'person'. ")
    if which_type == 'book':
        sortby = input("To sort by title: type 'title'. To sort by author: type 'author' "
                       "To sort by genre: type 'genre'. ")
        if sortby == 'title':
            sortType("title", "book")
        elif sortby == 'author':
            sortType("author", "book")
        elif sortby == 'genre':
            sortType("genre", "book")
        else:
            print("That is not an option... ")
    elif which_type == 'person':
        psortby = input("To sort by name: type 'name'. To sort by age: type 'age' "
                         "To sort by number of books: type '#books'. ")
        if psortby == 'name':
            sortType("name", "person")
        elif psortby == 'age':
            sortType("age", "person")
        elif psortby == '#books':
            sortType("#books", "person")
        else:
            print("That is not an option... ")

while True:
    answer = input("Do you want to show the state of the system. If yes: type 'yes'. If no: type anything else. ")
    if answer == "yes":
        showFullState()

    name = eval((input("\nWho would you like to interact with (type in the person's name): ")).lower())

    print(name.getName() + " is asking for a book")
    name.askBook()
    print("\n")
    printState()

    cont = input("To continue: type 'yes'. To stop: type anything else. ")
    if cont != "yes":
        break