import tkinter as tk
from tkinter import messagebox

# Sample data structure to hold book records
books = []

# Function to add a new book
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    
    if title and author and year:
        books.append({'Title': title, 'Author': author, 'Year': year})
        messagebox.showinfo("Success", "Book added successfully!")
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
        entry_year.delete(0, tk.END)
        display_books()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Function to display books in the listbox
def display_books():
    listbox_books.delete(0, tk.END)
    for book in books:
        book_info = f"{book['Title']} by {book['Author']} ({book['Year']})"
        listbox_books.insert(tk.END, book_info)

# Function to remove a selected book
def remove_book():
    selected_book_index = listbox_books.curselection()
    if selected_book_index:
        books.pop(selected_book_index[0])
        display_books()
        messagebox.showinfo("Success", "Book removed successfully!")
    else:
        messagebox.showwarning("Selection Error", "Please select a book to remove.")

# Setting up the main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("500x400")

# Labels and entry widgets for book information
tk.Label(root, text="Book Title").grid(row=0, column=0, padx=10, pady=5)
entry_title = tk.Entry(root)
entry_title.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Author").grid(row=1, column=0, padx=10, pady=5)
entry_author = tk.Entry(root)
entry_author.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Year").grid(row=2, column=0, padx=10, pady=5)
entry_year = tk.Entry(root)
entry_year.grid(row=2, column=1, padx=10, pady=5)

# Buttons for adding and removing books
btn_add = tk.Button(root, text="Add Book", command=add_book)
btn_add.grid(row=3, column=0, padx=10, pady=10)

btn_remove = tk.Button(root, text="Remove Selected Book", command=remove_book)
btn_remove.grid(row=3, column=1, padx=10, pady=10)

# Listbox to display books
listbox_books = tk.Listbox(root, width=50, height=15)
listbox_books.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
