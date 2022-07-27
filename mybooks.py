from book import *

def list_all_books(conn,email):
    cursor=conn.cursor()
    try:
        cursor.execute('SELECT book_number, title,author,genre, description,pages,condition,cover, email,trade_type,cost FROM book WHERE email=%s and trade_type!=%s',(email,'Sold'))
        books=cursor.fetchall()
        # print(books)
        books_array=[]
        for book in books:
            print(book[0])
            books_array.append(Book(book[1],book[2],book[3],book[4],book[5],book[6],book[7],book[8],book[10],book[9],book[0]))
        cursor.close()
        return books_array
    except Exception as e:
        print(e)
        cursor.close()
        return None


def get_book(conn,book_number):
    cursor=conn.cursor()
    try:
        cursor.execute('SELECT book_number, title,author,genre, description,pages,condition,cover, email,trade_type,cost FROM book \
        WHERE book_number=%s',(book_number,))
        book=cursor.fetchone()
        return Book(book[1],book[2],book[3],book[4],book[5],book[6],book[7],book[8],book[10],book[9],book[0])

    except Exception as e:
        print(e)
        cursor.close()
        return None

def buy_book_list(conn,email):
    cursor=conn.cursor()
    try:
        cursor.execute('SELECT book_number, title,author,genre, description,pages,condition,cover, email,trade_type,cost FROM book \
        WHERE email!=%s and trade_type!=%s',(email,'Sold',))
        books=cursor.fetchall()
        books_array=[]
        for book in books:
            print(book[0])
            books_array.append(Book(book[1],book[2],book[3],book[4],book[5],book[6],book[7],book[8],book[10],book[9],book[0]))
        cursor.close()
        return books_array
    except Exception as e:
        print(e)
        cursor.close()
        return None

def buy_book(conn,book,email):
    cursor=conn.cursor()
    try:
        cursor.execute('UPDATE book SET trade_type=%s WHERE book_number=%s',('Sold',book.book_number,))
        conn.commit()
        cursor.execute('INSERT INTO alltrades(book_number,email,trade_date) VALUES(%s,%s,now())',(book.book_number,email,))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        cursor.close()
        return None