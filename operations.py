# operations.py
# All library system functions

# -----------------------------
# DATA STRUCTURES
# -----------------------------
books = {}  # {isbn: {"title": "", "author": "", "genre": "", "copies": int, "available": int}}
members = []  # list of dicts: [{"id": "", "name": "", "borrowed": []}]
genres = ["Fiction", "Non-Fiction", "Science", "History", "Sci-Fi"]

# -----------------------------
# CORE FUNCTIONS
# -----------------------------

def add_book(isbn, title, author, genre, copies):
    if isbn in books:
        return "Book already exists!"
    if genre not in genres:
        return "Invalid genre!"
    books[isbn] = {"title": title, "author": author, "genre": genre,
                   "copies": copies, "available": copies}
    return f"Book '{title}' added successfully!"

def add_member(member_id, name):
    for m in members:
        if m["id"] == member_id:
            return "Member already exists!"
    members.append({"id": member_id, "name": name, "borrowed": []})
    return f"Member '{name}' added successfully!"

def search_book(keyword):
    result = []
    for isbn, info in books.items():
        if keyword.lower() in info["title"].lower() or keyword.lower() in info["author"].lower():
            result.append(f"{info['title']} by {info['author']} | Genre: {info['genre']}")
    return result if result else ["No book found."]

def update_book(isbn, title=None, author=None, genre=None, copies=None):
    if isbn not in books:
        return "Book not found!"
    if title: books[isbn]["title"] = title
    if author: books[isbn]["author"] = author
    if genre: books[isbn]["genre"] = genre
    if copies:
        books[isbn]["copies"] = copies
        books[isbn]["available"] = copies
    return "Book updated successfully!"

def delete_book(isbn):
    if isbn in books:
        del books[isbn]
        return "Book deleted!"
    return "Book not found!"

def borrow_book(member_id, isbn):
    for m in members:
        if m["id"] == member_id:
            if isbn not in books:
                return "Book not found!"
            if books[isbn]["available"] <= 0:
                return "Book not available!"
            if len(m["borrowed"]) >= 3:
                return "Cannot borrow more than 3 books!"
            m["borrowed"].append(isbn)
            books[isbn]["available"] -= 1
            return f"{m['name']} borrowed '{books[isbn]['title']}'"
    return "Member not found!"

def return_book(member_id, isbn):
    for m in members:
        if m["id"] == member_id:
            if isbn in m["borrowed"]:
                m["borrowed"].remove(isbn)
                books[isbn]["available"] += 1
                return f"{m['name']} returned '{books[isbn]['title']}'"
            return "Book not borrowed!"
    return "Member not found!"