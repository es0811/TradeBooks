class Trade:
    def __init__(self,trade_number,role,date,book_title,counterparty):
        self.trade_number=trade_number
        self.role=role
        self.date=date
        self.book_title=book_title
        self.counterparty_email=counterparty

def get_trade(conn,email):
    cursor=conn.cursor()
    cursor.execute('SELECT alltrades.trade_number as tm, CASE \
        WHEN alltrades.email=%s THEN \'buyer\' \
                ELSE \'seller\' \
        END AS r, alltrades.trade_date as d, book.title as t, book.email as e FROM alltrades JOIN book ON book.book_number=alltrades.book_number WHERE alltrades.email=%s \
        UNION	\
        SELECT alltrades.trade_number as tm, CASE \
        WHEN alltrades.email=%s THEN \'buyer\' \
                ELSE \'seller\' \
        END AS r, alltrades.trade_date as d,book.title as t,alltrades.email as e FROM alltrades JOIN book ON book.book_number=alltrades.book_number WHERE book.email=%s',(email,email,email,email,))
    trades=cursor.fetchall()
    alltrades=[]
    print(trades)
    for t in trades:
        alltrades.append(Trade(t[0],t[1],t[2],t[3],t[4]))
    cursor.close()
    return alltrades

def books_bought(conn,email):
    cursor=conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM alltrades WHERE email=%s',(email,))
    count=cursor.fetchone()[0]
    cursor.close()
    return count

def books_sold(conn,email):
    cursor=conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM book WHERE email=%s and trade_type=%s',(email,'Sold'))
    count=cursor.fetchone()[0]
    cursor.close()
    return count
