from book import *

def get_buy_book_list(conn,email):
    cursor=conn.cursor()
    try:
        cursor.execute('SELECT book_number, title,author,genre, description,pages,condition,cover, email,trade_type FROM book WHERE email!=%s and trade_type=%s',(email,'Sell',))
        books=cursor.fetchall()
        # print(books)
        books_array=[]
        for book in books:
            print(book[0])
            books_array.append(Book(book[1],book[2],book[3],book[4],book[5],book[6],book[7],book[8],book[9],book[0]))
        cursor.close()
        return books_array
    except Exception as e:
        print(e)
        cursor.close()
        return None


def get_sell_your_book_list(conn,email):
    cursor=conn.cursor()
    try:
        cursor.execute('SELECT book_number, title,author,genre, description,pages,condition,cover, email,trade_type FROM book WHERE email=%s and trade_type=%s',(email,'Sell',))
        books=cursor.fetchall()
        # print(books)
        books_array=[]
        for book in books:
            print(book[0])
            books_array.append(Book(book[1],book[2],book[3],book[4],book[5],book[6],book[7],book[8],book[9],book[0]))
        cursor.close()
        return books_array
    except Exception as e:
        print(e)
        cursor.close()
        return None
