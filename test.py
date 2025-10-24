
# Testing all functions in the Library System

from operations import *

print(" RUNNING FUNCTION TESTS")

# 1️ Add Books
print(add_book("B10", "think like a man", "Petros joel", "Non-Fiction", 4))
print(add_book("B11", "dont cross kesuma", "MR alaki bad", "fiction", 2))

# Add Members
print(add_member("M10", "caroline"))
print(add_member("M11", "florence"))

#  Search Book
print("Searching for 'Code':")
print(search_book("Code"))

#  Borrow Book
print("Borrow Book:")
print(borrow_book("M10", "B10"))
print(borrow_book("M11", "B11"))

#  Return Book
print("Return Book:")
print(return_book("M11", "B11"))

#  Update and Delete Book
print("Update/Delete:")
print(update_book("B10", copies=5))
print(delete_book("B11"))

#  Display Data
print("Current Books List:")
print(books)

print("Current Members List:")
print(members)