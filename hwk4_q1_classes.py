class Node:
    numMade = 0
    def __init__(self, data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous
        self.ID = Node.numMade
        Node.numMade += 1

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setPrevious(self, previous):
        self.previous = previous

    def getPrevious(self):
        return self.previous

class List:
    def __init__(self):
        self.size = 0
        self.front = None
        self.back = None

    def getFront(self):
        return self.front

    def setFront(self,front):
        self.front = front

    def getBack(self):
        return self.back

    def setBack(self, back):
        self.back = back

    def getSize(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def append(self, data):
        '''adds the data to a node to the end of the list'''
        if self.isEmpty():
            self.front = Node(data)
            self.back = self.front
            self.size += 1
        else:
            temp = Node(data)
            self.getBack().setNext(temp)
            temp.setPrevious(self.back)
            self.back = temp
            self.size += 1

    def remove(self, data):
        ''' removes a particular data point'''
        x = self.getFront()
        while x != None:
            if self.size == 1:  # only one item in the list
                if x.getData() == data:
                    self.setFront(None)
                    self.setBack(None)
                    self.size -= 1
            elif x.getPrevious() == None:  # it's the first item in the list
                if x.getData() == data:
                    self.setFront(x.getNext())
                    x.getNext().setPrevious(None)
                    self.size -= 1
            elif x.getNext() == None:  # it's the last item in the list
                if x.getData() == data:
                    self.setBack(x.getPrevious())
                    x.getPrevious().setNext(None)
                    self.size -= 1
            elif x.getData() == data:  # it's in the middle of the list
                x.getPrevious().setNext(x.getNext())
                x.getNext().setPrevious(x.getPrevious())
                self.size -= 1
            x = x.getNext()

    def find(self, thing):
        ''' finds and returns the node the data is in'''
        curr = self.getFront()
        for i in range(self.getSize()):
            if curr.getData() == thing:
                return curr
            else:
                curr = curr.getNext()
        return None

    def printList(self, type1):
        ''' prints the list of names of the object'''
        list = ""
        x = self.getFront()
        if type1 == "name":
            for i in range(self.getSize()):
                list += x.getData().getName() + ", "
                x = x.getNext()
        return(list)

    def index(self, input):
        ''' returns the data at a certain index'''
        counter = 0
        current = self.getFront()
        for i in range(self.getSize()):
            if input == counter:
                return current.getData()
            current = current.getNext()
            counter += 1

    def clear(self):
        ''' clears the list'''
        self.front = None
        self.back = None

class Person:
    numMade = 0
    def __init__(self, name, age, people_list, all_books):
        self.name = name
        self.age = age
        self.friends = List()
        self.books = List()
        self.book_history = List()
        self.ID = Person.numMade
        self.all_books = all_books
        self.left = None
        self.right = None
        people_list.append(self)
        Person.numMade += 1

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, new):
        self.left = new

    def setRight(self, new):
        self.right = new

    def hasLeft(self):
        return self.left != None

    def hasRight(self):
        return self.right != None

    def getID(self):
        return self.ID

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getNumBooks(self):
        return self.books.getSize()

    def getFriends(self):
        return self.friends

    def getBookHistory(self):
        return self.book_history

    def getBooks(self):
        return self.books

    def hasFriend(self, friend):
        if self.getFriends().find(friend) != None:
            return True
        else:
            return False

    def hasBook(self, book):
        if self.getBooks().find(book) != None:
            return True
        else:
            return False

    def addFriend(self, friend):
        ''' adds the friend if they don't already have it'''
        if self.hasFriend(friend):
            print("He/she is already your friend...")
        else:
            self.getFriends().append(friend)

    def removeFriend(self, friend):
        ''' removes the friend if they have it'''
        if self.hasFriend(friend):
            self.friends.remove(friend)
        else:
            print("He/she is not your friend...")

    def addBook(self, book):
        ''' adds the book if they don't already have it'''
        if self.hasBook(book):
            print("This person already has that book")
        else:
            self.getBooks().append(book)
            if self.getBookHistory().find(book) == None:
                self.getBookHistory().append(book)

    def removeBook(self, book):
        ''' removes the book if they have it'''
        if self.hasBook(book):
            self.getBooks().remove(book)
        else:
            print(self.getName() + " doesn't have this book...")

    def askBook(self):
        ''' the person asks for a book and then this prompts the giveBook() function'''
        keyword = input("Type in the title, author, or genre of the book: ")
        matches = List()
        currentNode = self.all_books.getFront()
        for i in range(self.all_books.getSize()):
            if keyword.lower() in currentNode.getData().getDescription().lower():
                if matches.find(currentNode.getData()) == None:
                    matches.append(currentNode.getData())
            currentNode = currentNode.getNext()
        if matches.getSize() != 0:
            print(matches.printList("name"))
            answer = int(input("Which book do you want to read: for first, Type: '1'. for second, Type: '2'. etc. "))
            if answer <= matches.getSize():
                self.giveBook(matches.index(answer - 1))
            else:
                print("That is not one of the options...")
        else:
            print("Sorry there were no matches...")


    def giveBook(self, book):
        ''' removes the book from the person who has it and adds it to self'''
        curr_person = self.getFriends().getFront()
        for i in range(self.getFriends().getSize()):
            curr_book = curr_person.getData().getBooks().getFront()
            for j in range(curr_person.getData().getBooks().getSize()):
                if curr_book.getData() == book:
                    curr_person.getData().removeBook(curr_book.getData())
                    self.addBook(curr_book.getData())
                    print("\n" + curr_person.getData().getName() + " gave " + self.getName() + " '" + curr_book.getData().getName() + "'")
                    rating = float(input("What would you rate this book (on a scale of 1 to 5): "))
                    if book.getAnnotation() == False:
                        annotate = input("Do you want to annotate this book. If yes: type 'yes'. If no: type 'no'. ")
                        if annotate == "yes":
                            book.updateAnnotation()
                    else:
                        print("This book is already annotated")
                    book.updateRating(rating)
                    print(book.getName() + " rating: " + str(book.getRating()))
                    print(book.getName() + " annotated << " + str(book.getAnnotation()) + " >>")
                    return True
                curr_book = curr_book.getNext()
            curr_person = curr_person.getNext()
        print("None of your friends have this book")


class Book:
    numMade = 0
    def __init__(self, title, author, genre, edition, book_list, rate = None, annotation = False, num_ratings = 1):
        self.title = title
        self.author = author
        self.genre = genre
        self.edition = edition
        self.annotation = annotation
        self.rating = rate
        self.num_ratings = num_ratings
        self.ID = Book.numMade
        self.left = None
        self.right = None
        book_list.append(self)
        Book.numMade += 1

    def getID(self):
        return self.ID

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, new):
        self.left = new

    def setRight(self, new):
        self.right = new

    def hasLeft(self):
        return self.left != None

    def hasRight(self):
        return self.right != None

    def getDescription(self):
        return self.title + "," + self.author + "," + self.genre

    def getName(self):
        return self.title

    def getRating(self):
        return self.rating

    def getAnnotation(self):
        return self.annotation

    def getAuthor(self):
        return self.author

    def getGenre(self):
        return self.genre

    def getEdition(self):
        return self.edition

    def updateRating(self, new_rating):
        ''' averages out all of the ratings and updates the rating attribute'''
        if new_rating >= 1 and new_rating <= 5:
            if self.rating == None:
                self.rating = new_rating
            else:
                self.num_ratings += 1
                self.rating = (self.rating + new_rating) / self.num_ratings
        else:
            print("The rating must be between 1 and 5")

    def updateAnnotation(self):
        self.annotation = True

class PersonTree:
    def __init__(self):
        self.root = None
        self.allPeople = List()
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def emptyTree(self):
        self.size = 0
        self.root = None
        self.allPeople.clear()

    def include(self, D, type):  # helper function for the recursive insert function
        ''' this inserts D into the correct place in the Tree '''
        if self.isEmpty():
            self.root = D
            self.allPeople.append(self.root)
            self.size = self.size + 1
        else:
            self.insert(D, self.root, type)

    def insert(self, data, node, type):
        '''inserts a node in the tree'''
        if self.getTypeBoolean(data, node, type):
            if node.getLeft() != None:
                self.insert(data, node.getLeft(), type)
            else:
                node.setLeft(data)
                self.size = self.size + 1
                self.allPeople.append(node.getLeft())
        else:
            if node.getRight() != None:
                self.insert(data, node.getRight(), type)
            else:
                node.setRight(data)
                self.size = self.size + 1
                self.allPeople.append(node.getRight())

    def startOrderedList(self, type):
        ''' function to start the getOrderedList() function'''
        temp = List()
        if self.isEmpty():
            print("The tree was empty")
            return temp
        else:
            return self.getOrderedList(temp, self.root, type)

    def getOrderedList(self, list, node, type):
        ''' creates and returns the empty list'''
        if node.hasLeft():
            list = self.getOrderedList(list, node.getLeft(), type)
        self.getTypeValue(list, node, type)
        if node.hasRight():
            list = self.getOrderedList(list, node.getRight(), type)
        return list

    def getTypeBoolean(self, newPerson, person, type):
        ''' returns how the person wants to sort for medium brother'''
        if type == 'name':
            return newPerson.getName() < person.getName()
        if type == 'age':
            return newPerson.getAge() < person.getAge()
        if type == '#books':
            return newPerson.getNumBooks() < person.getNumBooks()

    def getTypeValue(self, temp, person, type):
        ''' prints out the sorted list based on what they are trying to sort by'''
        string = ''
        if type == 'name':
            string += "Name: " + person.getName() + "\t"
            string += "Age: " + str(person.getAge()) + "\t"
            string += "# Books: " + str(person.getNumBooks()) + "\t"
        if type == 'age':
            string += "Age: " + str(person.getAge()) + "\t"
            string += "Name: " + person.getName() + "\t"
            string += "# Books: " + str(person.getNumBooks()) + "\t"
        if type == '#books':
            string += "# Books: " + str(person.getNumBooks()) + "\t"
            string += "Name: " + person.getName() + "\t"
            string += "Age: " + str(person.getAge()) + "\t"
        temp.append(string)


class BookTree:
    def __init__(self):
        self.root = None
        self.allBooks = List()
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def emptyTree(self):
        self.size = 0
        self.root = None
        self.allBooks.clear()

    def include(self, D, type):  # helper function for the recursive insert function
        ''' this inserts D into the correct place in the Binary Search Tree '''
        if self.isEmpty():
            self.root = D
            self.allBooks.append(self.root)
            self.size = self.size + 1
        else:
            self.insert(D, self.root, type)

    def insert(self, data, node, type):
        if self.getTypeBoolean(data, node, type):
            if node.getLeft() != None:
                self.insert(data, node.getLeft(), type)
            else:
                node.setLeft(data)
                self.size = self.size + 1
                self.allBooks.append(node.getLeft())
        else:
            if node.getRight() != None:
                self.insert(data, node.getRight(), type)
            else:
                node.setRight(data)
                self.size = self.size + 1
                self.allBooks.append(node.getRight())

    def startOrderedList(self, type):
        temp = List()
        if self.isEmpty():
            print("The tree was empty")
            return temp
        else:
            return self.getOrderedList(temp, self.root, type)

    def getOrderedList(self, list, node, type):
        if node.hasLeft():
            list = self.getOrderedList(list, node.getLeft(), type)
        self.getTypeValue(list, node, type)
        if node.hasRight():
            list = self.getOrderedList(list, node.getRight(), type)
        return list

    def getTypeBoolean(self, newBook, book, type):
        if type == 'title':
            return newBook.getName() < book.getName()
        if type == 'author':
            return newBook.getAuthor() < book.getAuthor()
        if type == 'genre':
            return newBook.getGenre() < book.getGenre()
        if type == 'rating':
            return newBook.getRating() < book.getRating()

    def getTypeValue(self, temp, book, type):
        string = ''
        if type == 'title':
            string += "Title: " + book.getName() + "\t"
            string += "Author: " + book.getAuthor() + "\t"
            string += "Genre: " + book.getGenre() + "\t"
            string += "Rating: " + str(book.getRating) + "\t"
        if type == 'author':
            string += "Author: " + book.getAuthor() + "\t"
            string += "Title: " + book.getName() + "\t"
            string += "Genre: " + book.getGenre() + "\t"
            string += "Rating: " + str(book.getRating) + "\t"
        if type == 'genre':
            string += "Genre: " + book.getGenre() + "\t"
            string += "Title: " + book.getName() + "\t"
            string += "Author: " + book.getAuthor() + "\t"
            string += "Rating: " + str(book.getRating) + "\t"
        if type == 'rating':
            string += "Rating: " + str(book.getRating) + "\t"
            string += "Title: " + book.getName() + "\t"
            string += "Author: " + book.getAuthor() + "\t"
            string += "Genre: " + book.getGenre() + "\t"

        temp.append(string)