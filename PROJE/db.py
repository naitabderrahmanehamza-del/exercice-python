import sqlite3
from typing import List, Tuple


def get_connection(db_name: str = "library.db"):
    return sqlite3.connect(db_name)


def init_database(db_name: str = "library.db"):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            isbn TEXT UNIQUE,
            available INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrow (
            borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            book_id INTEGER NOT NULL,
            borrow_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            return_date TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (book_id) REFERENCES books(book_id)
        )
    ''')
    
    conn.commit()
    conn.close()


def add_student(name: str, email: str = "", phone: str = "", db_name: str = "library.db") -> int:
    conn = get_connection(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO students (name, email, phone)
            VALUES (?, ?, ?)
        ''', (name, email, phone))
        student_id = cursor.lastrowid
        conn.commit()
        return student_id
    except sqlite3.IntegrityError:
        raise ValueError("Email already exists")
    finally:
        conn.close()


def get_all_students(db_name: str = "library.db") -> List[Tuple]:
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT student_id, name, email, phone FROM students ORDER BY name')
    results = cursor.fetchall()
    conn.close()
    return results


def delete_student(student_id: int, db_name: str = "library.db"):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
    conn.commit()
    conn.close()


def add_book(title: str, author: str = "", isbn: str = "", db_name: str = "library.db") -> int:
    conn = get_connection(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO books (title, author, isbn)
            VALUES (?, ?, ?)
        ''', (title, author, isbn))
        book_id = cursor.lastrowid
        conn.commit()
        return book_id
    except sqlite3.IntegrityError:
        raise ValueError("ISBN already exists")
    finally:
        conn.close()


def get_all_books(available_only: bool = False, db_name: str = "library.db") -> List[Tuple]:
    conn = get_connection(db_name)
    cursor = conn.cursor()
    if available_only:
        cursor.execute('''
            SELECT book_id, title, author, isbn, available 
            FROM books 
            WHERE available = 1
            ORDER BY title
        ''')
    else:
        cursor.execute('''
            SELECT book_id, title, author, isbn, available 
            FROM books 
            ORDER BY title
        ''')
    results = cursor.fetchall()
    conn.close()
    return results


def delete_book(book_id: int, db_name: str = "library.db"):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE book_id = ?', (book_id,))
    conn.commit()
    conn.close()


def borrow_book(student_id: int, book_id: int, db_name: str = "library.db") -> bool:
    conn = get_connection(db_name)
    cursor = conn.cursor()
    
    cursor.execute('SELECT available FROM books WHERE book_id = ?', (book_id,))
    result = cursor.fetchone()
    if not result or result[0] == 0:
        conn.close()
        return False
    
    cursor.execute('''
        INSERT INTO borrow (student_id, book_id)
        VALUES (?, ?)
    ''', (student_id, book_id))
    
    cursor.execute('UPDATE books SET available = 0 WHERE book_id = ?', (book_id,))
    
    conn.commit()
    conn.close()
    return True


def return_book(borrow_id: int, db_name: str = "library.db"):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    
    cursor.execute('SELECT book_id FROM borrow WHERE borrow_id = ?', (borrow_id,))
    result = cursor.fetchone()
    if result:
        book_id = result[0]
        
        cursor.execute('''
            UPDATE borrow SET return_date = CURRENT_TIMESTAMP
            WHERE borrow_id = ?
        ''', (borrow_id,))
        
        cursor.execute('UPDATE books SET available = 1 WHERE book_id = ?', (book_id,))
    
    conn.commit()
    conn.close()


def get_active_borrows(db_name: str = "library.db") -> List[Tuple]:
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT b.borrow_id, s.name, bk.title, b.borrow_date
        FROM borrow b
        JOIN students s ON b.student_id = s.student_id
        JOIN books bk ON b.book_id = bk.book_id
        WHERE b.return_date IS NULL
        ORDER BY b.borrow_date DESC
    ''')
    results = cursor.fetchall()
    conn.close()
    return results


def get_all_borrows(db_name: str = "library.db") -> List[Tuple]:
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT b.borrow_id, s.name, bk.title, b.borrow_date, b.return_date
        FROM borrow b
        JOIN students s ON b.student_id = s.student_id
        JOIN books bk ON b.book_id = bk.book_id
        ORDER BY b.borrow_date DESC
    ''')
    results = cursor.fetchall()
    conn.close()

    return results
