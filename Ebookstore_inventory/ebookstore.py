import sqlite3

# Connect to database
conn = sqlite3.connect('ebookstore.db')
c = conn.cursor()

# Create table
c.execute('''
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    qty INTEGER NOT NULL
)
''')

# Insert initial data
books = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]

c.executemany('INSERT OR REPLACE INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)', books)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

# Define functions for each operation
def enter_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter quantity: "))
    c.execute("INSERT OR REPLACE INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)", (id, title, author, qty))
    conn.commit()
    conn.close()
    print("Book entered successfully!")

def update_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    id = int(input("Enter book ID to update: "))
    title = input("Enter new title: ")
    author = input("Enter new author: ")
    qty = int(input("Enter new quantity: "))
    c.execute("UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?", (title, author, qty, id))
    conn.commit()
    conn.close()
    print("Book updated successfully!")

def delete_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    id = int(input("Enter book ID to delete: "))
    c.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print("Book deleted successfully!")

def search_books():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    id = int(input("Enter book ID to search: "))
    c.execute("SELECT * FROM book WHERE id = ?", (id,))
    book = c.fetchone()
    conn.close()
    if book:
        print(f"Book found: ID is {book[0]}, Title is {book[1]}, Author is {book[2]}, Quantity is {book[3]}")
    else:
        print("NO book not found.")

# Menu
def menu():
    while True:
        print("\n1. Enter book\n2. Update book\n3. Delete book\n4. Search books\n0. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            enter_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
