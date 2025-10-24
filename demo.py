# demo.py
# Demonstration of the Library System

from operations import *

print(" MINI LIBRARY SYSTEM DEMO")

# Add Members
print(add_member("M01", "Joel"))
print(add_member("M02", "Michelle"))

# Add Books
print(add_book("B01", "closet chronicles", "Mr joelpk", "fiction", 3))
print(add_book("B02", "Think like a billionaire", "Mr petros", "Sci-Fi", 2))

# Search
print(" Search Results:")
for b in search_book("Python"):
    print("-", b)

# Borrow and Return
print(" Borrow/Return:")
print(borrow_book("M01", "B01"))
print(borrow_book("M02", "B02"))
print(return_book("M02", "B02"))

# Update and Delete
print("Updates:")
print(update_book("B01", author="Mr joelpk"))
print(delete_book("B02"))

# Display current data
print(" Current Books:")
for isbn, data in books.items():
    print(isbn, ":", data)

print("Current Members:")
for m in members:
    print(m)