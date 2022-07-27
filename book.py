class Book:
    def __init__(self,title,author,genre,description,pages,condition,cover,email, cost,trade_type='Sell',book_number=None):
        self.book_number=book_number
        self.title=title
        self.author=author
        self.genre=genre
        self.description=description
        self.pages=pages
        self.condition=condition
        self.cover=cover
        self.email=email
        self.trade_type=trade_type
        self.cost=cost

    def list(self,conn):
        cursor=conn.cursor()
        print('cost')
        print(self.cost)

        try:
            cursor.execute('INSERT INTO book(title,author,genre, description,pages, condition,cover, email,trade_type,cost)\
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.title,self.author,self.genre,self.description, self.pages, self.condition, self.cover, self.email, self.trade_type,self.cost))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
        cursor.close()
        return False
