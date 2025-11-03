import tkinter as tk
from tkinter import ttk, messagebox
import db


class LibraryApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("ENSAM Library Management")
        self.root.geometry("1000x700")
        
        db.init_database()
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.create_students_tab()
        self.create_books_tab()
        self.create_borrow_tab()
    
    def create_students_tab(self):
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="Students")
        
        input_frame = ttk.LabelFrame(tab_frame, text="Add Student", padding=10)
        input_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.student_name_entry = ttk.Entry(input_frame, width=30)
        self.student_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Email:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.student_email_entry = ttk.Entry(input_frame, width=30)
        self.student_email_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Phone:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.student_phone_entry = ttk.Entry(input_frame, width=30)
        self.student_phone_entry.grid(row=2, column=1, padx=5, pady=5)
        
        add_button = ttk.Button(input_frame, text="Add Student", command=self.add_student)
        add_button.grid(row=3, column=1, pady=10)
        
        list_frame = ttk.LabelFrame(tab_frame, text="Students List", padding=10)
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        columns = ('ID', 'Name', 'Email', 'Phone')
        self.students_table = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.students_table.heading(col, text=col)
            self.students_table.column(col, width=150)
        
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.students_table.yview)
        self.students_table.configure(yscrollcommand=scrollbar.set)
        
        self.students_table.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        refresh_button = ttk.Button(list_frame, text="Refresh", command=self.refresh_students)
        refresh_button.pack(pady=5)
        
        delete_button = ttk.Button(list_frame, text="Delete Selected", command=self.delete_student)
        delete_button.pack(pady=5)
        
        self.refresh_students()
    
    def create_books_tab(self):
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="Books")
        
        input_frame = ttk.LabelFrame(tab_frame, text="Add Book", padding=10)
        input_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(input_frame, text="Title:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.book_title_entry = ttk.Entry(input_frame, width=30)
        self.book_title_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Author:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.book_author_entry = ttk.Entry(input_frame, width=30)
        self.book_author_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="ISBN:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.book_isbn_entry = ttk.Entry(input_frame, width=30)
        self.book_isbn_entry.grid(row=2, column=1, padx=5, pady=5)
        
        add_button = ttk.Button(input_frame, text="Add Book", command=self.add_book)
        add_button.grid(row=3, column=1, pady=10)
        
        list_frame = ttk.LabelFrame(tab_frame, text="Books List", padding=10)
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        columns = ('ID', 'Title', 'Author', 'ISBN', 'Available')
        self.books_table = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.books_table.heading(col, text=col)
            self.books_table.column(col, width=150)
        
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.books_table.yview)
        self.books_table.configure(yscrollcommand=scrollbar.set)
        
        self.books_table.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        refresh_button = ttk.Button(list_frame, text="Refresh", command=self.refresh_books)
        refresh_button.pack(pady=5)
        
        delete_button = ttk.Button(list_frame, text="Delete Selected", command=self.delete_book)
        delete_button.pack(pady=5)
        
        self.refresh_books()
    
    def create_borrow_tab(self):
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="Borrow/Return")
        
        borrow_frame = ttk.LabelFrame(tab_frame, text="Borrow Book", padding=10)
        borrow_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(borrow_frame, text="Student:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.student_combobox = ttk.Combobox(borrow_frame, width=27, state='readonly')
        self.student_combobox.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(borrow_frame, text="Book:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.book_combobox = ttk.Combobox(borrow_frame, width=27, state='readonly')
        self.book_combobox.grid(row=1, column=1, padx=5, pady=5)
        
        borrow_button = ttk.Button(borrow_frame, text="Borrow Book", command=self.borrow_book_action)
        borrow_button.grid(row=2, column=1, pady=10)
        
        list_frame = ttk.LabelFrame(tab_frame, text="All Borrow Records", padding=10)
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        columns = ('ID', 'Student', 'Book', 'Borrow Date', 'Return Date')
        self.borrows_table = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.borrows_table.heading(col, text=col)
            if col == 'Return Date':
                self.borrows_table.column(col, width=150)
            else:
                self.borrows_table.column(col, width=180)
        
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.borrows_table.yview)
        self.borrows_table.configure(yscrollcommand=scrollbar.set)
        
        self.borrows_table.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        refresh_button = ttk.Button(list_frame, text="Refresh", command=self.refresh_borrows)
        refresh_button.pack(pady=5)
        
        return_button = ttk.Button(list_frame, text="Return Selected", command=self.return_book_action)
        return_button.pack(pady=5)
        
        self.refresh_borrows()
    
    def add_student(self):
        name = self.student_name_entry.get().strip()
        email = self.student_email_entry.get().strip()
        phone = self.student_phone_entry.get().strip()
        
        if not name:
            messagebox.showerror("Error", "Name is required!")
            return
        
        try:
            db.add_student(name, email, phone)
            messagebox.showinfo("Success", "Student added successfully!")
            self.student_name_entry.delete(0, 'end')
            self.student_email_entry.delete(0, 'end')
            self.student_phone_entry.delete(0, 'end')
            self.refresh_students()
            self.refresh_borrow_combos()
        except ValueError as error:
            messagebox.showerror("Error", str(error))
    
    def refresh_students(self):
        for row in self.students_table.get_children():
            self.students_table.delete(row)
        
        students = db.get_all_students()
        
        for student in students:
            self.students_table.insert('', 'end', values=student)
    
    def delete_student(self):
        selected_items = self.students_table.selection()
        
        if not selected_items:
            messagebox.showwarning("Warning", "Please select a student to delete")
            return
        
        selected_row = self.students_table.item(selected_items[0])
        student_id = selected_row['values'][0]
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            db.delete_student(student_id)
            messagebox.showinfo("Success", "Student deleted successfully!")
            self.refresh_students()
            self.refresh_borrow_combos()
    
    def add_book(self):
        title = self.book_title_entry.get().strip()
        author = self.book_author_entry.get().strip()
        isbn = self.book_isbn_entry.get().strip()
        
        if not title:
            messagebox.showerror("Error", "Title is required!")
            return
        
        try:
            db.add_book(title, author, isbn)
            messagebox.showinfo("Success", "Book added successfully!")
            self.book_title_entry.delete(0, 'end')
            self.book_author_entry.delete(0, 'end')
            self.book_isbn_entry.delete(0, 'end')
            self.refresh_books()
            self.refresh_borrow_combos()
        except ValueError as error:
            messagebox.showerror("Error", str(error))
    
    def refresh_books(self):
        for row in self.books_table.get_children():
            self.books_table.delete(row)
        
        books = db.get_all_books()
        
        for book in books:
            book_id = book[0]
            title = book[1]
            author = book[2]
            isbn = book[3]
            available = book[4]
            
            if available == 1:
                available_text = "Yes"
            else:
                available_text = "No"
            
            self.books_table.insert('', 'end', values=(book_id, title, author, isbn, available_text))
    
    def delete_book(self):
        selected_items = self.books_table.selection()
        
        if not selected_items:
            messagebox.showwarning("Warning", "Please select a book to delete")
            return
        
        selected_row = self.books_table.item(selected_items[0])
        book_id = selected_row['values'][0]
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this book?"):
            db.delete_book(book_id)
            messagebox.showinfo("Success", "Book deleted successfully!")
            self.refresh_books()
            self.refresh_borrow_combos()
    
    def refresh_borrow_combos(self):
        students = db.get_all_students()
        student_options = []
        for student in students:
            student_id = student[0]
            student_name = student[1]
            student_options.append(f"{student_id}: {student_name}")
        
        self.student_combobox['values'] = student_options
        
        books = db.get_all_books(available_only=True)
        book_options = []
        for book in books:
            book_id = book[0]
            book_title = book[1]
            book_options.append(f"{book_id}: {book_title}")
        
        self.book_combobox['values'] = book_options
    
    def borrow_book_action(self):
        student_selection = self.student_combobox.get()
        book_selection = self.book_combobox.get()
        
        if not student_selection or not book_selection:
            messagebox.showerror("Error", "Please select both student and book")
            return
        
        student_id = int(student_selection.split(':')[0])
        book_id = int(book_selection.split(':')[0])
        
        success = db.borrow_book(student_id, book_id)
        
        if success:
            messagebox.showinfo("Success", "Book borrowed successfully!")
            self.refresh_books()
            self.refresh_borrows()
            self.refresh_borrow_combos()
        else:
            messagebox.showerror("Error", "Book is not available!")
    
    def refresh_borrows(self):
        for row in self.borrows_table.get_children():
            self.borrows_table.delete(row)
        
        borrows = db.get_all_borrows()
        
        for borrow in borrows:
            borrow_id = borrow[0]
            student_name = borrow[1]
            book_title = borrow[2]
            borrow_date = borrow[3]
            return_date = borrow[4]
            
            if return_date is None:
                return_date = "Not returned"
            
            self.borrows_table.insert('', 'end', values=(borrow_id, student_name, book_title, borrow_date, return_date))
        
        self.refresh_borrow_combos()
    
    def return_book_action(self):
        selected_items = self.borrows_table.selection()
        
        if not selected_items:
            messagebox.showwarning("Warning", "Please select a borrow record to return")
            return
        
        selected_row = self.borrows_table.item(selected_items[0])
        borrow_id = selected_row['values'][0]
        return_date = selected_row['values'][4]
        
        if return_date != "Not returned":
            messagebox.showwarning("Warning", "This book has already been returned")
            return
        
        if messagebox.askyesno("Confirm", "Return this book?"):
            db.return_book(borrow_id)
            messagebox.showinfo("Success", "Book returned successfully!")
            self.refresh_books()
            self.refresh_borrows()
            self.refresh_borrow_combos()


root = tk.Tk()
app = LibraryApp(root)
root.mainloop()
