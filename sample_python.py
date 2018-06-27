import math
import random
from datetime import datetime

books = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
books_sorted = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana", "Jackal"]


##########
# O(1)
##########
def getBooks():
  return books


##########
# O(n)
##########
def getNumBooks():
  num_books = 0
  for book in books:
    num_books += 1
  return num_books

def getLowercaseBooks():
  lowercase_books = books
  book_index = 0
  for book in books:
    lowercase_books[book_index] = lowercase_books[book_index].lower()
    book_index += 1
  return lowercase_books

def hasBook(book_name):
  for book in books:
    if book == book_name:
      return True
  return False

def findBook(book_name):
  book_index = 0
  for book in books:
    if book == book_name:
      return book_index
    book_index += 1
  return -1

def shuffleBooks():
  num_books = getNumBooks()
  for i in xrange(num_books):
    random_i = random.randrange(num_books)
    temp_storage = books[i]
    books[i] = books[random_i]
    books[random_i] = temp_storage


##########
# O(n^2)
##########

# Give me a list of all possible book pairs
def printBookPairs():
  for book1 in books:
    for book2 in books:
      print book1 + " - " + book2



# Give me a list of all possible book triples
def printBookTriples():
  for book1 in books:
    for book2 in books:
      for book3 in books:
        print book1 + " - " + book2 + " - " + book3



##########
# O(2^n)
##########

# Give me all possible combination of books
def getListOfCheckoutCombos(l):
  list_length = getLengthOfList(l)
  if list_length == 0:
    return [ [] ]
  else:
    checkoutCombos = []
    previousCombos = getListOfCheckoutCombos( l[1:] )
    for combo in previousCombos:
      checkoutCombos.append( combo )
      checkoutCombos.append( combo + [l[0]] )
    return checkoutCombos



##########
# O(n!)
##########

# Give me all possible combination of books
def getAllOrderings(l):
  list_length = getLengthOfList(l)
  if list_length <= 1:
    return [l]
  else:
    orderings = []
    previousOrderings = getAllOrderings( l[1:] )
    for previousOrdering in previousOrderings:
      for i in xrange(getLengthOfList(previousOrdering) + 1):
        orderings.append( previousOrdering[i:] + [l[0]] + previousOrdering[:i] )
    return orderings



def getLengthOfList(l):
  list_length = 0
  for i in l:
    list_length += 1
  return list_length



start_time = datetime.now()
x=getAllOrderings(books + ["Kangaroo"])
end_time = datetime.now()
print end_time - start_time


# 9
# 362880
# 0:00:01.203865

# 10
# 3628800
# 0:00:09.603591

# 11
# 39916800
# 0:02:40.727259







